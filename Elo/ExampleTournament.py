from Tournament import Tournament, elo_ranks
from random import gauss, randint

players = ["Alice","Bob","Carol","David","Eve","Frank"]
skill = [1, 2, 1.5, 1.3, .8, .7]
T = Tournament(players)

for i in range(500):
    p1 = randint(0,5)
    p2 = randint(0,5)
    
    sc1 = abs(gauss(skill[p1],.6))
    sc2 = abs(gauss(skill[p2],.6))

    
    T.update(players[p1],players[p2],sc1,sc2)
    
elo_ranks(T)