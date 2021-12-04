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

import os
import json
import datetime
from messages.question import question
from util.firebase import post_data
app = Flask(__name__)

line_bot_api = LineBotApi(
    'drC5T2zPKOG3fIpuHll2QyCIhUDumnQY2m6EHwbICfn259sg9zRrdIbQa+eAm+gN3oo/trEkzAi47pLDuikgDZlwhX+5PSiZo/XuNMBC24wcm3WeKj32YIrWVAbK+czzgSnhc+FkL/NulMVAq7Eu1Y9PbdgDzCFqoOLOYbqAITQ=')
handler = WebhookHandler('ade5c3146d69ae281a7175d9fa9e1a61')


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
    time = datetime.datetime.now()
    if (event.message.text == "Yes"):
        message = TextSendMessage(text="Good job.")
        print(event.source)
        post_data(userId, time)
    elif (event.message.text == "record"):
        message = FlexSendMessage(
            alt_text='hello',
            contents=question
        )
    elif (event.message.text == "No"):
        message = TextSendMessage(text="Fight")
    line_bot_api.reply_message(
        event.reply_token,
        message)


if __name__ == "__main__":
    app.run()
