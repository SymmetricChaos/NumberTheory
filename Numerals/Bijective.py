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
        
class BijectiveBase:
    
    def __init__(self,n,b=2):
        self.n = n
        self.b = b
    
    def __str__(self):
        return int_to_bijective(self.n,self.b)
    
    def __repr__(self):
        return int_to_bijective(self.n,self.b)
    
    def __add__(self,addend):
        assert self.b == addend.b
        return BijectiveBase(self.n+addend.n,self.b)
    
    def __mul__(self,addend):
        assert self.b == addend.b
        return BijectiveBase(self.n*addend.n,self.b)
    
    def __int__(self):
        return self.n
    
A = BijectiveBase(4354,5)
B = BijectiveBase(1726,5)
print(A)
print(B)
print(A+B)


#print(bijective_to_int("3122",3))
#print(int_to_bijective(98,3))