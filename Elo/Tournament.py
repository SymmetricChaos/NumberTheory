from EloSystem import elo_update, elo_expected
from GeneralUtils import sort_by_values
from random import random

class Tournament:
    
    def __init__(self,players,start_score=1000,K=32):
        self.elo = dict()
        self.standings = dict()
        for p in players:
            self.elo[p] = start_score
            self.standings[p] = [0,0,0]
        self.start_score = start_score
        self.K = K
    
    def update(self,match_list):
        
        P1,P2,P1wl,P2wl,P1maps,P2maps = match_list
        
        
        if P1 not in self.standings:
            raise Exception(f"Player {P1} unknown.")
        if P2 not in self.standings:
            raise Exception(f"Player {P2} unknown.")
        s = P1maps+P2maps
        a,b = elo_update(self.elo[P1],self.elo[P2],P1maps/s,P2maps/s,self.K)
#        s = P1wl+P2wl
#        a,b = elo_update(self.elo[P1],self.elo[P2],P1wl/s,P2wl/s,self.K)

        self.standings[P1][0] += P1wl
        self.standings[P1][1] += P2wl
        self.standings[P1][2] += P1maps-P2maps
        
        self.standings[P2][0] += P2wl
        self.standings[P2][1] += P1wl
        self.standings[P2][2] += P2maps-P1maps
        
        self.elo[P1] = a
        self.elo[P2] = b
        
    def predict(self,P1,P2):
        return elo_expected(self.elo[P1],self.elo[P2])


    def copy(self):
        T = Tournament([i for i in self.standings.keys()],self.start_score,self.K)
        T.elo = self.elo
        T.standings = self.standings
        return T


def elo_ranks(tournament):
    L = sort_by_values(tournament.elo)
    out = ""
    for i,j in reversed(L):
        out += f"{i}: {j}\n"
    print(out)

def safe_div(a,b):
    try:
        return a/b
    except:
        return a
    
def standings(tournament):
    L = sorted(tournament.standings.items(), key=lambda x: (safe_div(x[1][0],x[1][1]), x[1][2]))
    out = ""
    for i,j in reversed(L):
        out += f"{i}: {j}\n"
    print(out)
    

def simulate(tournament,L):
    T = tournament.copy()
    T.K = 0
    for players in L:
        p1p, p2p = T.predict(players[0],players[1])
        r = random()
        if r > p1p:
            p1w = 0
            p2w = 1
        else:
            p1w = 1
            p2w = 0
        fake_match = [players[0],players[1],p1w,p2w,r,1-r]
        T.update(fake_match)
    standings(T)