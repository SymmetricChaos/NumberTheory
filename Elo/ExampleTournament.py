from Tournament import Tournament, elo_ranks
from random import gauss, randint

players = ["Alice","Bob","Carol","David","Eve","Frank"]
skill =   [2.1,     2,    2.2,    3.5,    2,   1.7]
T = Tournament(players)

for i in range(500):
    p1 = randint(0,5)
    p2 = randint(0,5)
    
    sc1 = abs(gauss(skill[p1],.2))
    sc2 = abs(gauss(skill[p2],.2))

    
    T.update(players[p1],players[p2],sc1,sc2)
    
elo_ranks(T)

print(T.predict("Frank","David"))