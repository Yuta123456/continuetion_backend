import datetime
from messages.question import question
from linebot import (
    LineBotApi
)
from linebot.models import FlexSendMessage
import os
import sys
from constants.LINE_BOT import LINE_BOT_CHANNEL_TOKEN
from util.firebase import get_ids_of_all_line_user, get_user_notice_time
sys.path.append(os.getcwd())


line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)

message = FlexSendMessage(
    alt_text='アップデート情報です\n' +
    '・Webサイト上で通知時間、継続内容を変更できるようになりました。\n' +
    '・WebサイトのURLが変わりました。https://continuationapp.netlify.app',
    contents=question
)

user_ids = get_ids_of_all_line_user()
for user_id in user_ids:
    line_bot_api.push_message(user_id, message)
