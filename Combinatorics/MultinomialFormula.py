from Combinatorics import factorial
from GeneralUtils import prod

def multinomial_formula(X,P):
    s = sum(X)
    f = factorial(s)
    pr1 = prod( [factorial(x) for x in X] )
    pr2 = prod( [p**x for p,x in zip(P,X)] )
    return f/pr1*pr2