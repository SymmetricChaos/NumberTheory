from EgyptianFractions import egyptian_form_factoring, \
                              egyptian_form_splitting
from RationalsType import Rational
import random

def list_to_sum(L):
    return " + ".join(str(l) for l in L)


print("Splitting Method")
for i in range(5):

    
    D = random.randint(2,15)
    N = random.randint(2,D)
    
    A = Rational(N,D)
    if A.n == 1:
        continue
    else:
        print()
    
        E = egyptian_form_splitting(A)
        print(A," = ",list_to_sum(E))
        
        if sum(E) != A:
            raise Exception("SUM IS WRONG")


print("\n\nFactoring Method")
ctr = 0
while ctr < 5:
    
    D = random.randint(2,100)
    N = random.randint(2,D)
    
    A = Rational(N,D)
    if A.n == 1:
        continue
    E = egyptian_form_factoring(A)
    
    if E == []:
        continue
    else:
        ctr += 1
        print()
        print(A," = ", list_to_sum(E))
        if sum(E) != A:
            raise Exception("SUM IS WRONG")
            