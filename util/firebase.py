import datetime

import json
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import os


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
    # TODO: pixelaへの投稿も必要。


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

def save_LINE_user_id_and_x_site_code(userId, prevent_X_site_request_forgery_code):
    access_info_ref = db.reference('/access_info').child("x_site_code_to_firebase_id")
    
    firebase_id = access_info_ref.child(prevent_X_site_request_forgery_code).get()
    if not firebase_id:
        # エラーを投げるようにした方が良い。
        return False
    
    access_info_ref = db.reference('/access_info').child("firebase_id_to_line_id")
    
    access_info_ref.update({
        firebase_id:userId
    })
    return True

def is_exists_x_site_code(prevent_X_site_request_forgery_code):
    access_info_ref = db.reference('/access_info').child("x_site_code_to_firebase_id")
    if access_info_ref.child(prevent_X_site_request_forgery_code).get():
        return True
    else:
        return False
    
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
    'databaseURL': 'https://continuation-5e078-default-rtdb.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
