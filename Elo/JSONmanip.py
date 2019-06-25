
def match_score(D):
    A = D["competitors"][0]["abbreviatedName"]
    B = D["competitors"][1]["abbreviatedName"]
    As = D["scores"][0]["value"]
    Bs = D["scores"][1]["value"]
    stg = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["number"]
    frm = D["bracket"]["stage"]["tournament"]["attributes"]["program"]["stage"]["format"]
    return A,B,As,Bs,stg, frm

def match_scores(js):
    out = []
    N = js["totalElements"]
    for i in range(N):
        D = js["content"][i]
        out.append( match_score(D) )
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
