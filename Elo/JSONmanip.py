
def match_score(D):
    a = D["scores"][0]["value"]
    b = D["scores"][1]["value"]
    return a,b

def map_score(D):
    a = 0
    b = 0
    for i in D["games"]:
        a += i["points"][0]
        b += i["points"][1]
    return a,b

def match_values(D):
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    As,Bs = match_score(D)
    Bs = D["scores"][1]["value"]
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    frm = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["format"]
    return A,B,As,Bs,stg, frm


def all_matches(js,score_type="matches"):
    out = []
    N = js["totalElements"]
    
    for i in range(N):
        D = js["content"][i]
        if D["status"] == "CONCLUDED":
            out.append( match_values(D) )
    return out

def stage_regular(L,n):
    out = []
    for i in L:
        if i[5] == "regular_season":
            if i[4] == n:
                out.append(i)
    return out
                
def stage_playoff(L,n):
    out = []
    for i in L:
        if i[5] == "title_matches":
            if i[4] == n:
                out.append(i)
    return out
