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


#R = "reviews"
#J = WKrequest(R,wktoken)
#print(J["data"][0])

for i in range(440,450):

    J = WKrequest(f"subjects/{i}",wktoken)
    
    ch = J["data"]["characters"]
    rd = J["data"]["readings"][0]["reading"]
    print(ch,rd)
#    print(J["object"])