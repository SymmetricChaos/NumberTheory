from  math  import  sqrt,floor,gcd,log
import  numpy.linalg  as  npla
import  numpy  as  np
from PrimeNumbers import primes

#  http://blog.fkraiem.org/2013/12/07/factoring-integers-factor-bases/
#  http://blog.fkraiem.org/2013/12/08/factoring-integers-dixons-algorithm/

#  To  start  with  we  need  to  produce  an  exponent  vector  for  smooth  numbers.  
#  For  example  4116  =  2*2*3*7*7*7  so  its  vector  would  be  (2,1,0,3)
#  This  function  returns  the  relevant  list  if  the  number  is  smooth  and  an  empty  list  otherwise
def prime_exponent_vector(x,P):
    out = [0]*len(P)
    n = 0
    for i in P:
        while x % i == 0:
            x //= i
            out[n] += 1
        n += 1
    if x != 1:
        return []
    return out

def vec2num(L,P):
    out = 1
    for i,j in zip(L,P):
        out *= j**i
    return out
    
#  Now  the  exponent  vector  of  the  product  of  two  numbers  is  the  sum  of  their  exponent  vectors
#  This  is  important  because  by  definition  a  number  is  square  if  every  element  of  the  exponent
#  vector  is  even.

P = [2,3,5,7,11,13]
print(42,prime_exponent_vector(42,P))
print(1050,prime_exponent_vector(1050,P))
print(42*1050,prime_exponent_vector(42*1050,P))
print("\n")

def dixon(N,P,S):
    
    factor_base = []
    for i in primes():
        if i > P:
            break
        factor_base.append(i)
    
    sN = floor(sqrt(N))+1
    L = []
    K = []
    # Search for smooth numbers
    for i in range(sN,N):
        x = (i*i) % N
        B = prime_exponent_vector(x,factor_base)
        if len(B)  >  0:
            L.append(np.array(B))
            K.append(i)
        if len(L) == S:
            break
    
    for i in range(S):
        for j in  range(i):
            if  sum((L[i]+L[j]) % 2) == 0:
                A,B = K[i],K[j]
                X = (L[i]+L[j])//2
                z1 = A*B%N
                z2 = vec2num(X,factor_base)
                g = gcd(z1-z2,N)
                if g != 1 and g !=  N:
                    return  g,N//g


N = 2276097836
#N = 84923
P = 50
S = 100
out = dixon(N,P,S)
print("Two factors  of {} are {}".format(N,out))

I = 2.7**sqrt(log(N)*log(log(N)))
print("Ideal  Factor  Base  Approximately {}".format(int(I)))
