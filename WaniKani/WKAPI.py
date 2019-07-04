import requests
import json
from WKtoken import wktoken

def WKrequest(S,token):
    wkurl = "https://api.wanikani.com/v2/"
    resp = requests.get(wkurl+S,headers=token)
    J = json.loads(resp.content.decode('utf-8'))
    return J

J = WKrequest("level_progressions",wktoken)

for i in J:
    print(i)

for i in J["data"]:
    print(i)
    print()
    
    
