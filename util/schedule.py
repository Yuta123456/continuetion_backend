import datetime
from linebot import (
    LineBotApi
)
from linebot.models import FlexSendMessage
import os
import sys
sys.path.append(os.getcwd())
from messages.question import question
from constants.LINE_BOT import LINE_BOT_CHANNEL_TOKEN
from util.firebase import get_ids_of_all_line_user, get_user_notice_time, needs_notice_for_user


line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)

message = FlexSendMessage(
    alt_text='今日はいかがでしたか？',
    contents=question
)

dt_now = datetime.datetime.now()
hour = dt_now.hour
user_ids = get_ids_of_all_line_user()
for user_id in user_ids:
    needs_notice = needs_notice_for_user(user_id)
    is_user_notice_time = get_user_notice_time(user_id) == hour
    if needs_notice_for_user and is_user_notice_time:
        line_bot_api.push_message(user_id, message)
