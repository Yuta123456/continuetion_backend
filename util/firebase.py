import json
import re
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import os

from util.message import get_restart_send_message, get_stop_send_message


def exist_today_data(userId, day):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    print(users_ref.child(day).get())
    if users_ref.child(day).get():
        return True
    else:
        return False


def post_firebase(userId, day):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    users_ref.update({
        day: True
    })


def show_data(userId):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    user_continuetion = users_ref.order_by_key().get()
    string = "直近一週間の結果"
    for key, val in user_continuetion.items():
        year = key[:4]
        month = key[4:6]
        day = key[6:]
        string += "\n{0}年{1}月{2}日 : {3}".format(year, month, day, "✅" if val else "❌")
    return string

def set_continuation_contents(userId, message): 
    # format set:{}
    contents = re.findall("set:(.*)", message)[0]
    users_ref = db.reference('/users').child(userId)
    users_ref.update({
        "contents": contents
    })
    return contents

def get_continuation_contents(userId):
    users_ref = db.reference('/users').child(userId)
    contents = users_ref.child("contents").get()
    return contents


def stop_send_message(userId):
    users_ref = db.reference('/users').child(userId)
    users_ref.update({
        "isCanSendMessage": False
    })
    message = get_stop_send_message()
    return message


def restart_send_message(userId):
    users_ref = db.reference('/users').child(userId)
    users_ref.update({
        "isCanSendMessage": True
    })
    message = get_restart_send_message()
    return message

def is_can_send_message_for_user(user_id):
    users_ref = db.reference('/users').child(user_id)
    is_can_send_message = users_ref.child("isCanSendMessage").get()
    print(is_can_send_message)
    if is_can_send_message:
        return True
    else:
        return False


def get_ids_of_all_line_user():
    users_ids = db.reference('/users').get()
    return list(users_ids)


json_path = './util/seckey.json'
if not os.path.exists(json_path):
    config = {
        "type": os.environ['type'],
        "project_id": os.environ['project_id'],
        "private_key_id": os.environ['private_key_id'],
        "private_key": os.environ['private_key'].replace("\\n", "\n"),
        "client_email": os.environ['client_email'],
        "client_id": os.environ['client_id'],
        "auth_uri": os.environ['auth_uri'],
        "token_uri": os.environ['token_uri'],
        "auth_provider_x509_cert_url": os.environ['auth_provider_x509_cert_url'],
        "client_x509_cert_url": os.environ['client_x509_cert_url']
    }
    with open(json_path, 'w') as f:
        json.dump(config, f)
with open(json_path, 'r') as f:
    data = json.load(f)
cred = credentials.Certificate(json_path)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://continuation-5e078-default-rtdb.firebaseio.com/'
})
