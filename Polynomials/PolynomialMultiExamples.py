from PolynomialMultiType import Atom
    
a = Atom("a")
b = Atom("b")
c = Atom("c")


print(f"a = {a}")
print(f"a*b = {a*b}")
print(f"a*a = {a*a}")
print(f"a**3 = {a**3}")
print(f"1-a = {1-a}")
print(f"a*a+a*b = {a*a+a*b}")
X = (a*a+a*b) * (a-c)
print((a-b*c)**4)

P = a*b + b*c + c + a
Q = c + a

print(P)
print(Q)