from Computation import fermats_method, fermat_and_trial
from time import time

n = 80460230041

print('Searching for a factor of {}'.format(n))

print("Using Fermat's method only:")
t0 = time()
a = fermats_method(n)
t1 = time()
print("Found {} in {} seconds\n\n".format(a,t1-t0))

print("Using Fermat's method switching to trial division:")
t0 = time()
a = fermat_and_trial(n)
t1 = time()
print("Found {} in {} seconds".format(a,t1-t0))
