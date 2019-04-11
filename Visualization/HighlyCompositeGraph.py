from Other.Factorization import factorization, prime_factorization
import matplotlib.pyplot as plt

N = []
L = []
Hn = [2]
Hl = [2]
for i in range(2,2000):
    f = len(factorization(i))
    N.append(i)
    L.append(f)
    
    if f > Hl[-1]:
        Hn.append(i)
        Hl.append(f)

print(Hn)

fig = plt.figure()
fig.set_size_inches(14, 6)
plt.bar(N,L,6)
plt.scatter(Hn,Hl,zorder=2)