from EgyptianFractions import egyptian_form_factoring, egyptian_split
from RationalsType import Rational
import random



print("Splitting Method")
for i in range(5):
    print()
    D = random.randint(3,100)
    A = Rational(2,D)
    E = egyptian_split(D)
    print(A," = ",E)
    if sum(E) != A:
        raise Exception("SUM IS WRONG")


print("\n\nFactoring Method")
for i in range(5):
    print()
    N = random.randint(2,100)
    D = random.randint(2,100)
    
    A = Rational(N,D)
    E = egyptian_form_factoring(A)
    
    if E == []:
        print(A,"does not work")
    else:
    
        print(A," = ", E)
        if sum(E) != A:
            raise Exception("SUM IS WRONG")