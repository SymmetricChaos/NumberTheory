from Other.Factorization import factorization, prime_factorization
import matplotlib.pyplot as plt

N = []
L = []
Hn = [2]
Hl = [1]
for i in range(2,200):
    f = len(factorization(i))
    N.append(i)
    L.append(f)
    
    if f > Hl[-1]:
        Hn.append(i)
        Hl.append(f)
    
plt.bar(N,L)
plt.scatter(Hn,Hl)