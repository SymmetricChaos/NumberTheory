import requests
import json
from WKtoken import wktoken

u = "https://api.wanikani.com/v2/level_progressions"
resp = requests.get(u,headers=wktoken)

J = json.loads(resp.content.decode('utf-8'))

for i in J:
    print(i)

for i in J["data"]:
    print(i)
    print()