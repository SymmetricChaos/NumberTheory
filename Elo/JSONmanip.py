def map_score(D):
    """Total points scored in a given series"""
    a = 0
    b = 0
    for i in D["games"]:
        a += i["points"][0]
        b += i["points"][1]
    return a,b

def match_score(D):
    """Total matches one"""
    a = D["scores"][0]["value"]
    b = D["scores"][1]["value"]
    return a,b

def series_score(D):
    """Returns 1 for winner and 0 for loser, .5 for ties"""
    a = D["scores"][0]["value"]
    b = D["scores"][1]["value"]
    if a > b:
        return 2,0
    if b > a:
        return 0,2

def match_values(D):
    """Name of each team, score for each team, stage number, match format"""
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    As1,Bs1 = match_score(D)
    As2,Bs2 = series_score(D)
    As,Bs = As1+As2, Bs1+Bs2
    Bs = D["scores"][1]["value"]
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    frm = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["format"]
    return A,B,As,Bs,stg, frm


def all_matches(js,score_type="matches"):
    """Return a list of match information for concluded matches"""
    out = []
    N = js["totalElements"]
    
    for i in range(N):
        D = js["content"][i]
        if D["status"] == "CONCLUDED":
            out.append( match_values(D) )
    return out

def stage_regular(L,n):
    """Extract the regular season matches from all_matches"""
    out = []
    for i in L:
        if i[5] == "regular_season":
            if i[4] == n:
                out.append(i)
    return out
                
def stage_playoff(L,n):
    """Extract the playoff matches from all_matches"""
    out = []
    for i in L:
        if i[5] == "title_matches":
            if i[4] == n:
                out.append(i)
    return out
