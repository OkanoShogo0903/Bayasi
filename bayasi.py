# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import sys
sys.path.append("C:\\Users\\okano\\Anaconda3\\Lib\\site-packages")
# C:\Users\okano\Anaconda3\Lib\site-packages
from datetime import datetime
import locale
import wave
import time
import threading
import random

print ("bot active")
print (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
print ("\n")
text = ["しーじ",
"シージ（小声）",
"シージすっか！",
"シージすっぞ",
"シージするかー",
"シージするらしーじ",
"はいはいみなさん、シージしますよー",
"バルキリーアイどこけ？",
"ばやシージ",
"５人でできるゲームか～、５人でできるゲームっていったら一体なんやろなー"
#"公式URL"
]

CK = 'Ie5H016sEX1S7rPa2H1xDzhjP'                             # Consumer Key
CS = 'pcWF2njdauUm2t3g5Pq4l2XxaPZOB1DRU6CVSsUlj64psVqVRJ'         # Consumer Secret
AT = '908126063284199425-ObKYdsMWZVL0dTNlSVr5f6qm5ZonQcf' # Access Token
AS = 'v3UV7IwKbGUJ0Qdg1HTtO8YZOjaLwV11AsaFbigmpeqkn'         # Accesss Token Secert

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

def tweet(hoge):
    global url
    global twitter
    params = {"status": hoge}
    req = twitter.post(url, params = params)

    # レスポンスを確認
    if req.status_code == 200:
        print ('OK: {0}'.format(hoge))
    else:
        print ("Error: %d" % req.status_code)

def bot_timer():
    b = datetime.now()
#    if(b.minute%10 == 0): # x分ごとの時報
    if(b.minute == 0): # 一時間ごとの時報
        rand_int = random.randint(0,len(text)-1)
        tweet(text[rand_int])
    # 呼び出された後の処理
    # 指定秒に呼び出されるようにスレッドをセットする
    t=threading.Timer(60,bot_timer)
    t.start()

if __name__ == '__main__':
    bot_timer()
