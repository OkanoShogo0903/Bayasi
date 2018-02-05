import requests
import json
import time
import threading
from datetime import datetime
import bayasi
# TODO : 
#   json file ,save and load
#   print score diff 
# 機能 :
#   今日のKDと勝ち負けの数、ヘッドショット率、プレイ時間を表示
username = "syababa"
platform = "uplay"

def requestPlayer(username, platform):
    r = requests.get('https://api.r6stats.com/api/v1/players/{}?platform={}'.format(username, platform))
    dict_ = r.json()

    if r.status_code == 404:
        return None
    else:
        return dict_

def Siege():
    data = requestPlayer(username,platform)
    player = data['player']
    d_win   = player['stats']['ranked']['wins'] - before['stats']['ranked']['wins']
    d_loss  = player['stats']['ranked']['losses'] - before['stats']['ranked']['losses']
    d_kill  = player['stats']['ranked']['kills'] - before['stats']['ranked']['kills']
    d_death = player['stats']['ranked']['deaths'] - before['stats']['ranked']['deaths']
    d_head  = player['stats']['overall']['headshots'] - before['stats']['overall']['headshots']
    d_time  = player['stats']['ranked']['playtime'] - before['stats']['ranked']['playtime']
 
    if d_time == 0:
        print("did not play game")
        return
    else:
        text = ""

        print('WIN : {0} ,LOSS: {1}'.format(d_win,d_loss))
        try:
            print('KD : {}'.format(d_kill/d_death))
        except:
            pass
        try:
            print('headshot : {}\%'.format( (headshots/d_kill)*100 ))
        except:
            pass
        print('プレイ時間 : {} (minute)'.format(d_time))
        
        text += "WIN : " + str(d_win) + " , LOSS : " + str(d_loss) + "\n"
        try:
            text += "KD : " + str(d_kill/d_death) + "\n"
        except:
            pass
        try:
            text += "HeadShot : " + str( (headshots/d_kill)*100 ) + "\n"
        except:
            pass
        text += "PlayTime : " + str(d_time) + "\n"

        bayasi.tweet(text)

def Thread():
    now = datetime.now()
    global username,platform
    global before
    # 記録
    if now.hour == 12 and now.minute == 0:
        data = requestPlayer(username,platform)
        before = data

    # 差分の取得と表示
    if(now.hour == 1 and now.minute == 0):
#    if(now.minute == 30):
        Siege()

#    print("Siege Thread Active ... minute : {}".format(now.minute))
    t=threading.Timer(60,Thread)
    t.start()

if __name__ == '__main__':
    d = requestPlayer("syababa","uplay")
    before = d['player']
#    data = requestPlayer("DarkKnight_haku","uplay")
    Thread()
    bayasi.bot_timer()
