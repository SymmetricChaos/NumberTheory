import json
from Tournament import Tournament, standings, simulate, montecarlo_simulate
from Elo.JSONmanip import all_matches, stage_regular, upcoming_matches

with open("OWLmatches.json", "r") as read_file:
    data = json.load(read_file)

S = all_matches(data)
stage_3 = stage_regular(S,3)


players = ["PHI","LDN","NYE","BOS","SEO","GLA","SHD","HZS",
           "TOR","HOU","ATL","FLA","DAL","SFS","CDH","GZC",
           "PAR","WAS","VAL","VAN"]

T = Tournament(players,K=40)
for match in stage_3:
    T.update(match[:6])

U = upcoming_matches(data)
stage_3u = stage_regular(U,3)
g = [(i[0],i[1]) for i in stage_3u]
#print("Possible Stage Final Standings")
#standings(simulate(T,g))

montecarlo_simulate(T,g,5)