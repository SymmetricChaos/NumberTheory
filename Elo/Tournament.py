from EloSystem import elo_update, elo_expected
from GeneralUtils import sort_by_values
from random import random
import copy

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
        
        # Calculate the score for the purpose of Elo
        # We give one point for each map win and four points for winning
        # This credits a team for their ability to win but also includes
        # information from how close the game was. Without the extra points
        # for winning scores would move extremely little since 4-0 shutouts
        # are so rare.
        s = P1maps+P2maps+4
        P1score = P1maps + 4*P1wl
        P2score = P2maps + 4*P2wl
        
        a,b = elo_update(self.elo[P1],self.elo[P2],P1score/s,P2score/s,self.K)

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
        T.elo = copy.deepcopy(self.elo)
        T.standings = copy.deepcopy(self.standings)
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
    # Copy the tournament so we don't modify what we have
    # Also set K to 0 to freeze rankings
    T = tournament.copy()
    T.K = 0
    for players in L:
        # Predict results
        p1p, p2p = T.predict(players[0],players[1])
        # Star score at zero
        p1s, p2s = 0,0
        for maps in range(4):
            r = random()
            if r > p1p:
                p1s += 1
            else:
                p2s += 1
        # Break a tie
        if p1s == p2s:
            r = random()
            if r > p1p:
                p1s += 1
            else:
                p2s += 1
        # determine winner
        if p1s > p2s:
            p2w = 0
            p1w = 1
        if p1s < p2s:
            p2w = 1
            p1w = 0
        # Update the tournament with fake data
        fake_match = [players[0],players[1],p1w,p2w,p1s,p2s]
        T.update(fake_match)
    return T
    
def montecarlo_simulate(tournament,L,N):
    T = tournament.copy()
    for i in range(N):
        S = simulate(T,L)
        pred = sorted(S.standings.items(), key=lambda x: (safe_div(x[1][0],x[1][1]), x[1][2]))
        print([i[0] for i in reversed(pred)])
    