
from Rationals import Rational, egyptian_form_factoring, egyptian_form_splitting, \
                      egyptian_form_greedy
from GeneralUtils import list_to_sum
import random

def egyptian_example(func,title="",failure_explanation="that don't work"):
    print(title)
    rounds = 0
    ctr = 0
    while ctr < 5:
        D = random.randint(2,50)
        N = random.randint(2,D)
        
        A = Rational(N,D)
        
        # Ignore unit fractions
        if A.n == 1:
            continue
        
        else:
            rounds += 1
            # Try to get an expansion
            E = func(A)
            if E != []:
                ctr += 1
                print()
                print(A," = ", list_to_sum(E))
                if sum(E) != A:
                    raise Exception("SUM IS WRONG")
    print("\n(Found {} fractions {})".format(rounds-ctr,failure_explanation))

egyptian_example(egyptian_form_factoring,"Factoring Method")
print("\n\n")
egyptian_example(egyptian_form_splitting,"Splitting Method","that would be too long")
print("\n\n")
egyptian_example(egyptian_form_greedy,"Greedy Method")
