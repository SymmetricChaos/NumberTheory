import json
from Tournament import Tournament
from Elo.JSONmanip import all_matches, stage_regular

with open("OWLmatches.json", "r") as read_file:
    data = json.load(read_file)

S = all_matches(data)
stage_1 = stage_regular(S,1)
stage_2 = stage_regular(S,2)
stage_3 = stage_regular(S,3)
stage_4 = stage_regular(S,4)

stages = [stage_1,stage_2,stage_3]

players = ["PHI","LDN","NYE","BOS","SEO","GLA","SHD","HZS",
           "TOR","HOU","ATL","FLA","DAL","SFS","CDH","GZC",
           "PAR","WAS","VAL","VAN"]



for n in range(3):
    T = Tournament(players,K=20)
    for i in stages[n]:
        T.update(i[0],i[1],i[2],i[3])
    print(f"Stage {n+1} Standings")
    print(T)


T = Tournament(players,K=20)
for n in range(3):
    for i in stages[n]:
        T.update(i[0],i[1],i[2],i[3])
print("Season Standings")
print(T)