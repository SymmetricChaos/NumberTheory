from GeneralUtils import equal_spacing

def ducci_step(L):
    out = []
    for i in range(len(L)):
        if i+1 == len(L):
            out.append( abs(L[0]-L[i]) )
            break
            
        out.append( abs(L[i]-L[i+1]) )
    return out

def ducci_sequence(L):
    L = L.copy()
    t = []
    yield L
    while L not in t:
        t.append(L)
        L = ducci_step(L)
#        if L in t:
#            break
        yield L

def show_ducci_sequence(L):
    w = max([len(str(i)) for i in L])+2
    for i in ducci_sequence(L):
        equal_spacing(i,w)

show_ducci_sequence([52,99,78,67,25])