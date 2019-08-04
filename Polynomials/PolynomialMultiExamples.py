from PolynomialMultiType import Atom
#from NumberTheory.Rationals import Rational

def atom_tests():
    print("Begin Atom Tests")
    a = Atom("a")
    b = Atom("b")
    val = [a,-a,a**3,a*a,a*b,1-a,a-1,a+a] 
    cor = ["a","-a","a^3","a^2","ab","-a + 1","a - 1","2a"]

    ctr = 0

    for test_val,correct_val in zip(val,cor):
        if str(test_val) != correct_val:
            print("Test Failed")
            print(f"{test_val} should show as {correct_val}")
            ctr += 1

    if ctr > 0:
        print(f"{ctr} Atom Tests Failed\n")
    else:
        print("All test passed\n")
    
    
def particle_tests():
    print("Begin Particle Tests")
    a = Atom("a")
    b = Atom("b")
    c = Atom("c")
    ab = a*b
    bc = c*b
    val = [ab,bc,ab+ab,ab+bc,2*ab,ab+a,a+ab,ab**2]
    cor = ["ab","bc","2ab","bc + ab","2ab","ab + a","ab + a","a^2b^2"]

    ctr = 0

    for test_val,correct_val in zip(val,cor):
        if str(test_val) != correct_val:
            print("Test Failed")
            print(f"{test_val} should show as {correct_val}")
            ctr += 1

    if ctr > 0:
        print(f"{ctr} Particle Tests Failed\n")
    else:
        print("All test passed\n")
    
def mvpoly_tests():
    print("Begin MVPoly Tests")
    a = Atom("a")
    b = Atom("b")
    c = Atom("c")
    
    ab = a*b
    P = ab + 2*c + 2
    Q = b**2 * c - 5

    
    val = [P,Q,-P,P*2,P*c,P*Q,P+ab,P-ab,P+2,P-2,2-P,a-P]
    cor = ["ab + 2c + 2",
           "b^2c - 5",
           "-ab - 2c - 2",
           "2ab + 4c + 4",
           "abc + 2c^2 + 2c",
           "ab^3c + 2b^2c^2 + 2b^2c - 5ab - 10c - 10",
           "2ab + 2c + 2",
           "2c + 2",
           "ab + 2c + 4",
           "ab + 2c",
           "-ab - 2c",
           "-ab - 2c + a - 2"]


    ctr = 0

    for test_val,correct_val in zip(val,cor):
        if str(test_val) != correct_val:
            print("Test Failed")
            print(f"{test_val} should show as {correct_val}")
            ctr += 1
    
    if ctr > 0:
        print(f"{ctr} MVPoly Tests Failed\n")
    else:
        print("All test passed\n")


atom_tests()
particle_tests()
mvpoly_tests()


print()
a = Atom("a")
b = Atom("b")
c = Atom("c")
X = (a*a+a*b) * (a-c+b)*c
print(X)
print()
print(X.evaluate({"a":2}))
print(X.evaluate({"b":-1,}))
print(X.evaluate({"c":-3}))
print(X.evaluate({"a":2,"b":-1}))
print(X.evaluate({"b":-1,"c":-3}))
print(X.evaluate({"a":2,"c":-3}))
print(X.evaluate({"a":2,"b":-1,"c":-3}))
print(X.derivative(["b","c"]))