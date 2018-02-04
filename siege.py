import requests
import json
import time
import threading
from datetime import datetime
# TODO : 
#   json file ,save and load
#   print score diff 
# $B5!G=(B :
#   $B:#F|$N(BKD$B$H>!$AIi$1$N?t!"%X%C%I%7%g%C%HN(!"%W%l%$;~4V$rI=<((B
username = "syababa"
platform = "uplay"

def requestPlayer(username, platform):
    r = requests.get('https://api.r6stats.com/api/v1/players/{}?platform={}'.format(username, platform))
    dict_ = r.json()

    if r.status_code == 404:
        return None
    else:
        return dict_

def Thread():
    now = datetime.now()
    global username,platform
    global before
    # $B5-O?(B
#    if now.hour == 12 and now.minute == 0:
    if now.minute == 0:
        data = requestPlayer(username,platform)
        before = data

    # $B:9J,$N<hF@$HI=<((B
#    if(now.hour == 1 and now.minute == 0):
    if(now.minute == 30):
        data = requestPlayer(username,platform)
        player = data['player']
        d_win   = player['stats']['ranked']['wins'] - before['stats']['ranked']['wins']
        d_loss  = player['stats']['ranked']['losses'] - before['stats']['ranked']['losses']
        d_kill  = player['stats']['ranked']['kills'] - before['stats']['ranked']['kills']
        d_death = player['stats']['ranked']['deaths'] - before['stats']['ranked']['deaths']
        d_head  = player['stats']['overrall']['headshots'] - before['stats']['overrall']['headshots']
        d_time  = player['stats']['ranked']['playtime'] - before['stats']['ranked']['playtime']
        
        print('$B>!GT%l!<%H(B : {}'.format(d_win/d_loss))
        print('KD : {}'.format(d_kill/d_death))
        print('headshot : {}\%'.format( (headshots/d_kill)*100 ))
        print('$B%W%l%$;~4V(B : {} (minute)'.format(d_time))

    print("threa active minute : {}".format(now.minute))
    t=threading.Timer(60,Thread)
    t.start()

if __name__ == '__main__':
    d = requestPlayer("syababa","uplay")
    before = d['player']
#    data = requestPlayer("DarkKnight_haku","uplay")
    Thread()
