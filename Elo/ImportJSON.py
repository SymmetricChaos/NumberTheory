import json

with open("OWLmatches.json", "r") as read_file:
    data = json.load(read_file)

for i in data:
    print(i)

def match_score(D):
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    As = D["scores"][0]["value"]
    Bs = D["scores"][1]["value"]
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    print(A,B,As,Bs,stg)

def match_scores(js):
    N = js["totalElements"]
    for i in range(N):
        D = js["content"][i]
        match_score(D)

#print(data["content"][0]["bracket"]["stage"]["title"])
match_scores(data)