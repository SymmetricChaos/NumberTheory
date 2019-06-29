def total_points(D):
    """Total points scored in a given series"""
    a = 0
    b = 0
    for i in D["games"]:
        a += i["points"][0]
        b += i["points"][1]
    return a,b

def maps_won(D):
    """Total matches one"""
    a = D["scores"][0]["value"]
    b = D["scores"][1]["value"]
    return a,b

def winner_loser(D):
    """Returns 1 for winner and 0 for loser, .5 for ties"""
    a = D["scores"][0]["value"]
    b = D["scores"][1]["value"]
    if a > b:
        return 1,0
    if b > a:
        return 0,1
    
def competitors(D):
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    frm = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["format"]
    return A,B,0,0,0,0,0,stg,frm

def match_values(D):
    """Name of each team, score for each team, stage number, match format"""
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    A_series, B_series = winner_loser(D)
    A_maps, B_maps = maps_won(D)
    A_points, B_points = total_points(D)
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    frm = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["format"]
    return A,B,A_series,B_series,A_maps,B_maps,A_points,B_points,stg,frm


def all_matches(js,score_type="matches"):
    """Return a list of match information for concluded matches"""
    out = []
    N = js["totalElements"]
    
    for i in range(N):
        D = js["content"][i]
        if D["status"] == "CONCLUDED":
            out.append( match_values(D) )
    return out

def upcoming_matches(js,score_type="matches"):
    """Return a list of match information for upcoming matches"""
    out = []
    N = js["totalElements"]
    
    for i in range(N):
        D = js["content"][i]
        if D["status"] != "CONCLUDED":
            out.append( competitors(D) )
    return out

def stage_regular(L,n):
    """Extract the regular season matches from all_matches"""
    out = []
    for i in L:
        if i[-1] == "regular_season":
            if i[-2] == n:
                out.append(i)
    return out
                
def stage_playoff(L,n):
    """Extract the playoff matches from all_matches"""
    out = []
    for i in L:
        if i[-1] == "title_matches":
            if i[-2] == n:
                out.append(i)
    return out
