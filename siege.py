import requests
import json
# TODO : 
#   json file ,save and load
#   print score diff 
def requestPlayer(username, platform):
    r = requests.get('https://api.r6stats.com/api/v1/players/{}?platform={}'.format(username, platform))
    dict_ = r.json()

    if r.status_code == 404:
        return None
    else:
        return dict_

if __name__ == '__main__':
    data = requestPlayer("DarkKnight_haku","uplay")
    print('json : {}'.format(type(data)))
#    print(data.)
