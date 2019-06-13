from Combinatorics import choose

def binomial_distribution(n,p):
    pmf = []
    for k in range(n+1):
        pmf.append( choose(n,k)*p**k*(1-p)**(n-k) )
    return pmf

print(binomial_distribution(20,.7))