from linebot import (
    LineBotApi
)
from linebot.models import FlexSendMessage
import os
import sys
from constants.LINE_BOT import LINE_BOT_CHANNEL_TOKEN
sys.path.append(os.getcwd())

from messages.question import question

line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)

message = FlexSendMessage(
    alt_text='今日はいかがでしたか？',
    contents=question
)

line_bot_api.broadcast(message)
