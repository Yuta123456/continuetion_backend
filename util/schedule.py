
from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage, FlexSendMessage
)
import os
import sys
sys.path.append(os.getcwd())

from messages.question import question

line_bot_api = LineBotApi(
    'drC5T2zPKOG3fIpuHll2QyCIhUDumnQY2m6EHwbICfn259sg9zRrdIbQa+eAm+gN3oo/trEkzAi47pLDuikgDZlwhX+5PSiZo/XuNMBC24wcm3WeKj32YIrWVAbK+czzgSnhc+FkL/NulMVAq7Eu1Y9PbdgDzCFqoOLOYbqAITQ=')

message = FlexSendMessage(
    alt_text='今日はいかがでしたか？',
    contents=question
)

line_bot_api.broadcast(message)
