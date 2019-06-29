from EloSystem import elo_update, elo_expected
from GeneralUtils import sort_by_values

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
        
        P1,P2,P1wl,P2wl,P1maps,P2maps,P1points,P2points,stg,frm = match_list
        
        
        if P1 not in self.standings:
            raise Exception(f"Player {P1} unknown.")
        if P2 not in self.standings:
            raise Exception(f"Player {P2} unknown.")
        s = P1maps+P2maps
#        s = P1wl+P2wl
        a,b = elo_update(self.elo[P1],self.elo[P2],P1maps/s,P2maps/s,self.K)
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
        return Tournament([i for i in self.standings.keys()],self.start_score,self.K)




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