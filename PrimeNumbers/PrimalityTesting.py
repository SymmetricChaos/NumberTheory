from time import time
from random import sample

#from PrimeNumbers.MillerRabinTest import miller_rabin_test
#from PrimeNumbers.LucasLehmerTest import lucas_lehmer_test
from PrimeNumbers.TrialDivision import trial_division_test, fermat_and_trial_test
from PrimeNumbers.Primes import primes

#print("Lets try checking some Mersenne numbers for primality!")
#from LucasLehmer import LLPrimality
#for i in range(2,1001):
#    x = (2**i)-1
#    prLL = LLPrimality(i)
#    prMR = miller_rabin_test(x)
#    
#    if prLL == False:
#        if prMR == True:
#            print("Miller Rabin incorrectly identifies 2^{}-1 as prime".format(i))
#        


#for i in range(3,110):
#    if lucas_lehmer_test(i):
#        print(f"2^{i}-1 = {2**i-1}")


prime_list = []
for p in primes():
    if p > 20000000:
        break
    prime_list.append(p)
print(len(prime_list))
ctr = 0
while ctr < 50:

    a,b = sample(prime_list,2)
    N = a*b
    print(a,b)
    print(N)
    ctr += 1
    t0 = time()
    trial_division_test(N)
    print(f"Trial Division {time()-t0:5f} seconds")
    
    t0 = time()
    fermat_and_trial_test(N,25)
    print(f"Fermat Trial   {time()-t0:5f} seconds")
    
    print()