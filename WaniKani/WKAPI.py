import requests
import json
from WKtoken import wktoken

def WKrequest(S):
    wkurl = "https://api.wanikani.com/v2/"
    resp = requests.get(wkurl+S,headers=wktoken)
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nMade request {wkurl+S}")
    return J

