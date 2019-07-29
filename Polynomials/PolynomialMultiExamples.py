from PolynomialMultiType import Atom
#from NumberTheory.Rationals import Rational
a = Atom("a")
b = Atom("b")
c = Atom("c")


print(f"a = {a}")
print(f"a*b = {a*b}")
print(f"a*a = {a*a}")
print(f"a**3 = {a**3}")
print(f"1-a = {1-a}")
print(f"a*a+a*b = {a*a+a*b}")
print((a-b*c)**4)


print()
X = (a*a+a*b) * (a-c)
print(X)
print(X.eval({"a":2,"b":1,"c":3}))
print(X.reduce({"a":2}))
print(X.reduce({"a":2,"c":3}))