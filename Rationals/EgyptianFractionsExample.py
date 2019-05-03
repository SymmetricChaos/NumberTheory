from EgyptianFractions import egyptian_form_factoring, egyptian_split
from RationalsType import Rational
import random

def list_to_sum(L):
    return " + ".join(str(l) for l in L)

print("Splitting Method")
for i in range(5):
    print()
    D = random.randint(3,100)
    A = Rational(2,D)
    E = egyptian_split(D)
    print(A," = ",list_to_sum(E))
    
    if sum(E) != A:
        raise Exception("SUM IS WRONG")


print("\n\nFactoring Method")
ctr = 0
while ctr < 5:
    N = random.randint(2,100)
    D = random.randint(2,100)
    
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