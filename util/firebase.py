from datetime import datetime, date, timedelta
import json
import re
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import os
from util.achives import check_achives

from util.message import get_restart_send_message, get_stop_send_message


def exist_today_data(userId, day):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    if users_ref.child(day).get():
        return True
    else:
        return False


def post_firebase(userId, day):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    users_ref.update({
        day: True
    })


def get_user_data(userId):
    users_ref = db.reference('/users').child(userId).get()
    users_ref = dict(users_ref)
    return users_ref


def get_contribute_count(userId):
    user_ref = db.reference('/users').child(userId)
    users_contribute = user_ref.child('continuetion').get()
    # print(len(list(users_contribute)))
    achives = user_ref.child("achives").get() and {}
    achives = check_achives(achives, users_contribute)
    user_ref.update({
        "achives": achives
    })

    return len(list(users_contribute))


def show_data(userId):
    message = "直近一週間の結果\n"
    today = datetime.today()
    last_week = [today - timedelta(days=i) for i in range(7)]
    for day in last_week:
        format_day = datetime.strftime(day, '%Y-%m-%d')
        key = datetime.strftime(day, '%Y%m%d')
        message += format_day + ":"
        if exist_today_data(userId, key):
            message += "✅"
        else:
            message += "❌"
        message += "\n"
    return message


def setting_data(setting_request):
    userId = setting_request['userId']
    content = setting_request['content']
    notice_time = setting_request['noticeTime']
    user_ref = db.reference('/users').child(userId)
    user_ref.update({
        "contents": content
    })
    user_ref.update({
        "noticeTime": notice_time
    })


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


def needs_notice_for_user(user_id):
    users_ref = db.reference('/users').child(user_id)
    is_can_send_message = users_ref.child("isCanSendMessage").get()
    if is_can_send_message:
        return True
    else:
        return False


def get_user_notice_time(user_id):
    user_ref = db.reference('/users').child(user_id)
    notice_time = user_ref.child("noticeTime").get()
    if not notice_time:
        return 0
    notice_time = notice_time.split(":")[0]
    return int(notice_time)


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
