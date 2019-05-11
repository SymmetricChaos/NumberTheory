from timeit import timeit
from random import sample
from PrimeNumbers.TrialDivision import trial_division_test, fermat_and_trial_test
from PrimeNumbers.MillerRabinTest import miller_rabin_test
from PrimeNumbers.Primes import primes

prime_list = []
for p in primes():
    if p > 10000000:
        break
    prime_list.append(p)

semiprime_list = []
for i in range(100):
    a,b = sample(prime_list,2)
    semiprime_list.append(a*b)

def test_trial_div():
    for i in semiprime_list:
        trial_division_test(i)
        
def test_fermat_and_trial():
    for i in semiprime_list:
        fermat_and_trial_test(i)
        
def test_miller_rabin():
    for i in semiprime_list:
        miller_rabin_test(i)

print(timeit("test_miller_rabin()", setup="from __main__ import test_miller_rabin",number=10))
print(timeit("test_trial_div()", setup="from __main__ import test_trial_div",number=10))
print(timeit("test_fermat_and_trial()", setup="from __main__ import test_fermat_and_trial",number=10))
