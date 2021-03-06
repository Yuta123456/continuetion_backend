import datetime
from flask import Flask, request, abort, jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
from messages.question import question
from util.firebase import exist_today_data, get_contribute_count, get_user_data, post_firebase, restart_send_message, set_continuation_contents, setting_data, show_data, stop_send_message
from util.message import get_fruits, get_no_reply_message, get_set_complete_message
from constants.LINE_BOT import LINE_BOT_CHANNEL_SECRET, LINE_BOT_CHANNEL_TOKEN
from flask_cors import CORS

app = Flask(__name__)
# 本番環境を追加
CORS(app, origins=[
     "https://continuationapp.netlify.app", "http://localhost:8100"])
line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)
handler = WebhookHandler(LINE_BOT_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def test():
    return 'test_v3'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@app.route("/userdata", methods=['GET'])
def user_data():
    request_data = request.args.to_dict()
    userId = request_data['userId']
    response = jsonify(get_user_data(userId))
    return response


@app.route("/setting", methods=['POST'])
def setting():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400
    setting_data(request.json)
    return (jsonify(res="success"),  200)


@app.route("/contributecount", methods=['GET'])
def contribute_count():
    request_data = request.args.to_dict()
    userId = request_data['userId']
    response = jsonify(get_contribute_count(userId))
    return response


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = None
    userId = event.source.sender_id
    # JSTとUTCの差分
    DIFF_JST_FROM_UTC = 9
    now = datetime.datetime.utcnow() + \
        datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    today = now.strftime('%Y%m%d')
    if event.message.text == "Yes":
        # 既に今日入力しているかどうか判定する
        if not exist_today_data(userId, today):
            message = TextSendMessage(
                text="すごい！偉いね✨\n https://continuationapp.netlify.app で確認もできるよ！")
            post_firebase(userId, today)
        else:
            message = TextSendMessage(text="今日の入力は終了しています！")
    elif event.message.text == "Record":
        message = FlexSendMessage(
            alt_text='今日はいかがでしたか？',
            contents=question
        )
    elif event.message.text == "No":
        message = TextSendMessage(text="🏳‍🌈明日は頑張ろう🏳‍🌈")
    elif event.message.text == "Show":
        message = TextSendMessage(text=show_data(userId))
    elif event.message.text == "Fruits":
        message = TextSendMessage(text=get_fruits())
    elif event.message.text.startswith("set:"):
        set_contents = set_continuation_contents(userId, event.message.text)
        message = TextMessage(text=get_set_complete_message(set_contents))
    elif event.message.text == "stop":
        message = stop_send_message(userId)
        message = TextMessage(text=message)
    elif event.message.text == "restart":
        message = restart_send_message(userId)
        message = TextMessage(text=message)
    else:
        message = TextSendMessage(text=get_no_reply_message())
    line_bot_api.reply_message(
        event.reply_token,
        message)


if __name__ == "__main__":
    app.run()
