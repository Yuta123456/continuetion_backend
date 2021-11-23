from flask import Flask, request, abort, Response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os
import json

app = Flask(__name__)

line_bot_api = LineBotApi(
    'drC5T2zPKOG3fIpuHll2QyCIhUDumnQY2m6EHwbICfn259sg9zRrdIbQa+eAm+gN3oo/trEkzAi47pLDuikgDZlwhX+5PSiZo/XuNMBC24wcm3WeKj32YIrWVAbK+czzgSnhc+FkL/NulMVAq7Eu1Y9PbdgDzCFqoOLOYbqAITQ=')
handler = WebhookHandler('ade5c3146d69ae281a7175d9fa9e1a61')


@app.route("/", methods=['GET'])
def test():
    return 'test'


@app.route("/", methods=['POST'])
def test2():
    return Response(response=json.dumps({'message': 'hello response'}), status=200)


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
    message = ""
    if (event.message.text == "Yes"):
        message = "Good job."
    else:
        message = "Fight!"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))


if __name__ == "__main__":
    #
    app.run()
#     {
#   "access_token": "drC5T2zPKOG3fIpuHll2QyCIhUDumnQY2m6EHwbICfn259sg9zRrdIbQa+eAm+gN3oo/trEkzAi47pLDuikgDZlwhX+5PSiZo/XuNMBC24wcm3WeKj32YIrWVAbK+czzgSnhc+FkL/NulMVAq7Eu1Y9PbdgDzCFqoOLOYbqAITQ=",
#   "expires_in": 2592000,
#   "token_type": "Bearer"
# }
