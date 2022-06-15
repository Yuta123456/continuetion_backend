import os
import sys
sys.path.append(os.getcwd())

from util.firebase import get_ids_of_all_line_user
from constants.LINE_BOT import LINE_BOT_CHANNEL_TOKEN
from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage
)

line_bot_api = LineBotApi(
    LINE_BOT_CHANNEL_TOKEN)

info = 'アップデート情報です\n' + \
    '・Webサイト上で通知時間、継続内容を変更できるようになりました。\n' + \
    "・この変更に伴い、Webサイト上で通知時間を設定しないと、明日から通知が来なくなります。（多分）\n" + \
    '・WebサイトのURLが変わりました。https://continuationapp.netlify.app'
message = TextSendMessage(text=info)

user_ids = get_ids_of_all_line_user()
for user_id in user_ids:
    print(user_id)
    try :
        line_bot_api.push_message(user_id, message)
    except Exception as e:
        print(e)
        pass
# user_id = "U306b245775fa454f21b86167dd665cff"
