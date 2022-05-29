from linebot import (
    LineBotApi
)
from linebot.models import FlexSendMessage
import os
import sys
from constants.LINE_BOT import LINE_BOT_CHANNEL_TOKEN
from util.firebase import get_ids_of_all_line_user, is_can_send_message_for_user
sys.path.append(os.getcwd())

from messages.question import question

line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)

message = FlexSendMessage(
    alt_text='今日はいかがでしたか？',
    contents=question
)

user_ids = get_ids_of_all_line_user()
for user_id in user_ids:
    if is_can_send_message_for_user(user_id):
        line_bot_api.push_message(user_id, message)