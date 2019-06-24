from EloSystem import elo_update, elo_expected
from GeneralUtils import sort_by_values

class Tournament:
    
    def __init__(self,players,start_score=2000,K=32):
        self.players = dict()
        for p in players:
            self.players[p] = start_score
        self.K = K
    
    def update(self,P1,P2,S1,S2):
        if P1 not in self.players:
            raise Exception("First player unknown.")
        if P2 not in self.players:
            raise Exception("First player unknown.")
        s = S1+S2
        a,b = elo_update(self.players[P1],self.players[P2],S1/s,S2/s,self.K)
        self.players[P1] = a
        self.players[P2] = b

def elo_ranks(tournament):
    p = tournament.players
    L = sort_by_values(p)
    for i in reversed(L):
        print(i)

#T = Tournament(["Alice","Bob"],32)
#
#print(T.players)
#T.update("Alice","Bob",1,50)
#print(T.players)