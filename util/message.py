import random
def get_fruits():
    fruits = ["🥝", "🍓", "🍒", "🍑", "🍏", "🍐","🍎","🥭","🍍", 
              "🍌", "🍊", "🍉", "🍈", "🍇"]
    return random.choice(fruits)
def get_no_reply_message():
    no_reply_message =  "そのメッセージは反応できないです。😰"
    no_reply_message += "\n反応できるメッセージ一覧"
    no_reply_message += "\nShow: 直近の継続データを表示します"
    no_reply_message += "\nRecord: 記録を取るためのメッセージを送ります"
    no_reply_message += "\nFruits: ランダムなフルーツを送ります"
    return no_reply_message