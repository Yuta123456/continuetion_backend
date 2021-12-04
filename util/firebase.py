import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


def post_data(userId, day):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    print(users_ref.child(day).get())
    if users_ref.child(day).get():
        return False
    users_ref.update({
        day: True
    })
    return True


def show_data(userId):
    users_ref = db.reference('/users').child(userId).child('continuetion')
    user_continuetion = users_ref.order_by_key()
    string = "直近一週間の結果\n"
    for key, val in user_continuetion.items():
        string += "{0} : {1}\n".format(key, "🔴" if val else "🔵")
    return string


cred = credentials.Certificate('./seckey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://continuation-5e078-default-rtdb.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
