import json
from Tournament import Tournament
from Elo.JSONmanip import match_scores, stage_regular

with open("OWLmatches.json", "r") as read_file:
    data = json.load(read_file)

S = match_scores(data)
stage_1 = stage_regular(S,1)
stage_2 = stage_regular(S,2)


players = ["PHI","LDN","NYE","BOS","SEO","GLA","SHD","HZS",
           "TOR","HOU","ATL","FLA","DAL","SFS","CDH","GZC",
           "PAR","WAS","VAL","VAN"]

T = Tournament(players,start_score=1000,K=32)

for i in stage_1:
    T.update(i[0],i[1],i[2],i[3])

print("Stage 1 Standings")
print(T)

T = Tournament(players,start_score=1000,K=32)

for i in stage_2:
    T.update(i[0],i[1],i[2],i[3])
    
print("Stage 2 Standings")
print(T)
    