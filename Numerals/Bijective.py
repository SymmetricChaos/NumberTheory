from math import ceil

def bijective_to_int(s,b):
    N = [int(i) for i in s]
    
    pws = range(0,len(N))
    out = 0
    for d,p in zip(N,reversed(pws)):
        out += d*b**p
    return out
    
def int_to_bijective_str(n,b,silent=False):
    assert b > 0, "Base must be greater than zero"
    if b >= 10 and not silent:
        print("Base uses multiple decimal digits. Reading may be ambigious.")
    S = []
    q0,q1 = n,0
    while n > 0:
        n = ceil(n/b)-1
        q1 = n
        S.append(str(q0-q1*b))
        q0 = q1
    return "".join(reversed(S))

def int_to_bijective_list(n,b):
    S = []
    q0,q1 = n,0
    while n > 0:
        n = ceil(n/b)-1
        q1 = n
        S.append(q0-q1*b)
        q0 = q1
    S.reverse()
    return S


class BijectiveBase:
    
    ALPHA = "123456789ABCDEFGHJKLMNOPQRSTUVWXYZ"
        
    def __init__(self,n,b=2):
        self.n = n
        self.b = b
        self.L = int_to_bijective_list(self.n,self.b)

    def __str__(self):
        return "".join([self.ALPHA[i-1] for i in self.L])
    
    def __repr__(self):
        return "".join([self.ALPHA[i-1] for i in self.L])
    
    def __add__(self,addend):
        assert self.b == addend.b
        return BijectiveBase(self.n+addend.n,self.b)
    
    def __mul__(self,addend):
        assert self.b == addend.b
        return BijectiveBase(self.n*addend.n,self.b)
        
    def __int__(self):
        return self.n
    
    
A = BijectiveBase(4354,20)
B = BijectiveBase(1726,20)
print(A," + ",B," = ",A+B)
BijectiveBase.ALPHA = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
print(A," + ",B," = ",A+B)
#print(bijective_to_int("3122",3))
#print(int_to_bijective(98,3))