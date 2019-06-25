from math import ceil

def elo_expected(A,B):
    expectedA = 1/(1+10**((B-A)/400))
    expectedB = 1/(1+10**((A-B)/400))
    return expectedA, expectedB



def elo_update(A,B,scoreA,scoreB,K=32):
    expectedA, expectedB = elo_expected(A,B)
    A = A + ceil(K*(scoreA-expectedA))
    B = B - ceil(K*(scoreA-expectedA))
    
    return A,B