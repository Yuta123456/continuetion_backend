from flask import Flask, request, abort, Response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import requests
import datetime
from messages.question import question
from util.firebase import exist_today_data, is_exists_x_site_code, post_data, post_firebase, save_LINE_user_id_and_x_site_code, show_data
from util.message import get_fruits, get_no_reply_message
from constants.LINE_BOT import LINE_BOT_CHANNEL_SECRET, LINE_BOT_CHANNEL_TOKEN
app = Flask(__name__)

line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)
handler = WebhookHandler(LINE_BOT_CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def test():
    return 'test'


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = None
    userId = event.source.sender_id
    # JSTとUTCの差分
    DIFF_JST_FROM_UTC = 9
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    today = now.strftime('%Y%m%d')
    if (event.message.text == "Yes"):
        # 既に今日入力しているかどうか判定する
        if not exist_today_data(userId, today):
            message = TextSendMessage(text="すごい！偉いね✨")
            post_firebase(userId, today)
            post_pixela(userId, today)
        else:
            message = TextSendMessage(text="今日の入力は終了しています！")
    elif (event.message.text == "Record"):
        message = FlexSendMessage(
            alt_text='hello',
            contents=question
        )
    elif (event.message.text == "No"):
        message = TextSendMessage(text="🏳‍🌈明日は頑張ろう🏳‍🌈")
    elif (event.message.text == "Show"):
        message = TextSendMessage(text=show_data(userId))
    elif (event.message.text == "Fruits"):
        message = TextSendMessage(text=get_fruits())
    else:
        message = TextSendMessage(text=get_no_reply_message())
    line_bot_api.reply_message(
        event.reply_token,
        message)

@app.route("/auth", methods=['POST'])
def auth():
    # https://example.com/auth?code=abcd1234&state=0987poi&friendship_status_changed=true
    # 認可コード取得
    authorization_code = request.args.get("code")
    # クロスサイトリクエストフォージェリ防止用の固有な英数字の文字列
    prevent_X_site_request_forgery_code = request.args.get("state")
    if (not is_exists_x_site_code(prevent_X_site_request_forgery_code)):
        # 失敗 コードは考える
        return 400
    # アクセストークン取得
    access_token = getLINEAccessToken(authorization_code)
    userId = getLINEProfile(access_token)
    save_LINE_user_id_and_x_site_code(userId, prevent_X_site_request_forgery_code)
    return 200
def getLINEAccessToken(authorization_code):
    url = "https://api.line.me/oauth2/v2.1/token"
    header = {
        'Content-Type' : 'application/x-www-form-urlencoded',
    }
    payload = {
        'grant_type': 'authorization_code',
        'code': 'authorization_code',
        'redirect_uri':"/auth" 
    }
    res = requests.post(url, headers=header, params=payload)
    
def getLINEProfile(access_token):
    url = "https://api.line.me/v2/profile"
    headers = {
        'Authorization': f"Bearer{access_token}",
    }
    res = requests.get(url, headers=headers)
    print(res.json())
    # TODO: json化した後どんな感じになるかわからないのでいったん保留
    # userId = res.json()
    
if __name__ == "__main__":
    app.run()
