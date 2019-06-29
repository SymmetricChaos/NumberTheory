from math import ceil


# FIDE style logistic function Elo prediction
def elo_expected(A,B,n=400):
    x = A-B
    ex = -(x/n)
    expectedA = 1/(1+10**ex)
    expectedB = 1 - expectedA
    return expectedA, expectedB


def elo_update(A,B,scoreA,scoreB,K=32):
    expectedA, expectedB = elo_expected(A,B)
    A = A + ceil(K*(scoreA-expectedA))
    B = B - ceil(K*(scoreA-expectedA))
    return A,B