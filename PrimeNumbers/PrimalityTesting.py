from time import time

from PrimeNumbers.MillerRabinTest import miller_rabin_test
from PrimeNumbers.LucasLehmerTest import lucas_lehmer_test
from PrimeNumbers.TrialFactorization import 

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


for i in range(3,110):
    if lucas_lehmer_test(i):
        print(f"2^{i}-1 = {2**i-1}")
