import requests
import json
from WKtoken import wktoken

def WKrequest(S,token):
    wkurl = "https://api.wanikani.com/v2/"
    resp = requests.get(wkurl+S,headers=token)
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nMade request {wkurl+S}")
    return J


R = "reviews"
J = WKrequest(R,wktoken)
print(J["data"][0])

for i in range(1,10):

    J = WKrequest(f"subjects/{i}",wktoken)
    
    print(J["data"]["characters"])