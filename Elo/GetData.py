import requests
import json

owl_url = "https://api.overwatchleague.com/matches"

resp = requests.get(owl_url)

J = json.loads(resp.content.decode('utf-8'))

with open('OWLmatches.json', 'w') as outfile:
    json.dump(J, outfile)