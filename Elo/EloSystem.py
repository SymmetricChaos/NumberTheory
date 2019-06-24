from math import ceil

def elo_expected(A,B):
    expectedA = 1/(1+10**((B-A)/400))
    expectedB = 1/(1+10**((B-A)/400))
    return expectedA, expectedB



def elo_update(A,B,scoreA,scoreB,K=32):
    expectedA, expectedB = elo_expected(A,B)
    A = A + ceil(K*(scoreA-expectedA))
    B = B + ceil(K*(scoreB-expectedB))
    
    return A,B

p1 = 1613
p2 = 1609
p3 = 1477
p4 = 1388
p5 = 1586
p6 = 1720
print(p1)
p1,p2 = elo_update(p1,p2,0,1)
p1,p3 = elo_update(p1,p3,.5,.5)
p1,p4 = elo_update(p1,p4,1,0)
p1,p5 = elo_update(p1,p5,1,0)
p1,p6 = elo_update(p1,p6,0,1)

print(p1)