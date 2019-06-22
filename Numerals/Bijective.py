from math import ceil

def bijective_to_int(s,b):
    N = [int(i) for i in s]
    
    pws = range(0,len(N))
    out = 0
    for d,p in zip(N,reversed(pws)):
        out += d*b**p
    return out
    
def int_to_bijective(n,b):
    S = []
    q0,q1 = n,0
    while n > 0:
        n = ceil(n/b)-1
        q1 = n
        S.append(str(q0-q1*b))
        q0 = q1
    return "".join(reversed(S))
        
    
print(bijective_to_int("3122",3))
print(int_to_bijective(98,3))
#class BijectiveBase