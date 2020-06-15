def ackerman(m,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))
    
def ackerman_3(m,n,p):
    if p == 0:
        return m+n
    if n == 0 and p == 1:
        return 0
    if n == 0 and p == 2:
        return 1
    if n == 0 and p >= 3:
        return m
    else:
        return ackerman_3(m,ackerman_3(m,n-1,p),p-1)

from MyOtherMathStuff.Utils.StringManip import innermost, left_string


def A_expand(M,N):
    if M == 0:
        return f"{N+1}"
    if N == 0:
        return f"A({M-1},1)"
    return f"A({M-1},A({M},{N-1}))"


def A_expand_recur(M,N):
    S = f"A({M},{N})"
    print(S)
    while "A" in S:
        bottom,_,_ = innermost(S,"A",")")[0]
        m = int(left_string(bottom,"(",",",inner=True)[0])
        n = int(left_string(bottom,",",")",inner=True)[0])
        bottom_ex = A_expand(m,n)
        S = S.replace(bottom,bottom_ex)
        print(S)
        
if __name__ == "__main__":
    A_expand_recur(1,2)