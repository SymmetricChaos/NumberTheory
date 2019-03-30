import sys
sys.setrecursionlimit(5000)

def hyper(a,b,n):
    #print(b)
    if n == 0:
        return b+1
    if n == 1 and b == 0:
        return a
    if n == 2 and b == 0:
        return 0
    if n >= 3 and b == 0:
        return 1
    else:
        return hyper(a,hyper(a,b-1,n),n-1)

#print(hyper(5,2,4))