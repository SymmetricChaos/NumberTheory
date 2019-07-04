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



J = WKrequest("reviews",wktoken)

for i in J["data"]:
    print(i)
    print()

J = WKrequest("study_materials/2559",wktoken)

for i in J["data"]:
    print(i)
    print()

    
    
