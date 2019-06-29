import json
from Tournament import Tournament, elo_ranks, standings, simulate
from Elo.JSONmanip import all_matches, stage_regular, upcoming_matches

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
    T = Tournament(players,K=40)
    for match in stages[n]:
        T.update(match[:6])
    print(f"Stage {n+1} Elo Standings")
    elo_ranks(T)
    print("Stage Standings")
    standings(T)


T = Tournament(players,K=40)
for n in range(3):
    for match in stages[n]:
        T.update(match[:6])
print("Season Elo Standings")
elo_ranks(T)
print("Season Standings")
standings(T)


U = upcoming_matches(data)
stage_3u = stage_regular(U,3)
g = [(i[0],i[1]) for i in stage_3u]
print("Possible Stage Final Standings")
simulate(T,g)