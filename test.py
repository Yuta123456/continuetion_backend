import datetime


# JSTとUTCの差分
DIFF_JST_FROM_UTC = 9
now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
today = now.strftime('%Y%m%d')
print(today)