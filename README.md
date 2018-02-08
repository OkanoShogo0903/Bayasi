# Bayasi Bot
BayasiegeBot for twitter  
Tweet Today Stats  
*Useing R6STATS-API* do not support by public  

## requirements
### 1. requests
pip install requests  
### 2. none
^^
## API
[R6STATS](https://r6stats.com/)  
## R6STATS JSON
it is sample
~~~
{'player':{  
    'username': 'syababa',  
    'platform': 'uplay',  
    'ubisoft_id': 'ac2b6e71-4789-4c64-a228-f73a37db0b32',  
    'indexed_at': '2018-02-04T04:12:42.008Z',  
    'updated_at': '2018-02-04T04:12:42.008Z',  
    'stats': {  
        'ranked':{  
            'has_played': True,  
            'wins': 964,  
            'losses': 870,  
            'wlr': 1.108,  
            'kills': 8776,  
            'deaths': 7574,  
            'kd': 1.159,  
            'playtime': 2351560  
        },  
        'casual': {  
            'has_played': True,  
            'wins': 436,   
            'losses': 446,   
            'wlr': 0.978,   
            'kills': 2364,   
            'deaths': 2463,   
            'kd': 0.96,   
            'playtime': 794033.0  
        },   
        'overall': {  
            'revives': 316,   
            'suicides': 33,   
            'reinforcements_deployed': 12952,   
            'barricades_built': 2657,   
            'steps_moved': -2144316615,   
            'bullets_fired': 440234,   
            'bullets_hit': 89861,   
            'headshots': 3469,   
            'melee_kills': 321,   
            'penetration_kills': 676,   
            'assists': 3261  
        },   
        'progression': {  
            'level': 204,  
            'xp': 49475  
        }  
    }  
}}  
~~~
