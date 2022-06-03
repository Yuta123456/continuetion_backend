import os
line_key_path = './constants/seckey.txt'
if os.path.exists(line_key_path):
    with open(line_key_path, mode='r') as f:
        key = [s for s in f.readlines()]
        LINE_BOT_CHANNEL_SECRET = key[0]
        LINE_BOT_CHANNEL_TOKEN  = key[1]
else:
    LINE_BOT_CHANNEL_SECRET = os.environ['LINE_BOT_CHANNEL_SECRET']
    LINE_BOT_CHANNEL_TOKEN  = os.environ['LINE_BOT_CHANNEL_TOKEN']

