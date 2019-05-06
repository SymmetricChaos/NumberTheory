from BisectionMethod import bisection_method_convergents

print("Finding the root of a polynomial by the bisection method")
f = lambda x : x**3 - x - 2
for i in bisection_method_convergents(1,10,f):
    print(i)