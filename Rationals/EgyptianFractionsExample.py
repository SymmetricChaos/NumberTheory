from EgyptianFractions import egyptian_form_factoring, \
                              egyptian_form_splitting
from RationalsType import Rational
import random

def list_to_sum(L):
    return " + ".join(str(l) for l in L)

def egyptian_example(func):
    ctr = 0
    while ctr < 5:
        D = random.randint(2,50)
        N = random.randint(2,D)
        
        A = Rational(N,D)
        
        if A.n == 1:
            continue
        
        else:
            E = func(A)
            if E != []:
                ctr += 1
                print()
                print(A," = ", list_to_sum(E))
                if sum(E) != A:
                    raise Exception("SUM IS WRONG")


print("Splitting Method")
egyptian_example(egyptian_form_splitting)


print("\n\nFactoring Method")
egyptian_example(egyptian_form_factoring)