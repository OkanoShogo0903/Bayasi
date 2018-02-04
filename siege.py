import requests
import json
def requestPlayer(username, platform):
    r = requests.get('https://api.r6stats.com/api/v1/players/{}?platform={}'.format(username, platform))
    json = r.json()

    if r.status_code == 404:
        return None
    else:
        return json

if __name__ == '__main__':
    data = requestPlayer("DarkKnight_haku","uplay")
    print(data)
