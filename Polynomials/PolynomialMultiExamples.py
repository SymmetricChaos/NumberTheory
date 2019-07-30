from PolynomialMultiType import Atom
#from NumberTheory.Rationals import Rational

def atom_tests():
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

    print(f"{ctr} Atom Tests Failed")
    
    
def particle_tests():
    a = Atom("a")
    b = Atom("b")
    c = Atom("c")
    ab = a*b
    bc = c*b
    val = [ab+ab,ab+bc,2*ab,ab+a]
    cor = ["2ab","bc + ab","2ab","ab + a"]

    ctr = 0

    for test_val,correct_val in zip(val,cor):
        if str(test_val) != correct_val:
            print("Test Failed")
            print(f"{test_val} should show as {correct_val}")
            ctr += 1

    print(f"{ctr} Particle Tests Failed")
    
#def mypoly_tests():
#    a = Atom("a")
#    b = Atom("b")
#    c = Atom("c")
#
#    val = []
#    cor = []
#
#    ctr = 0
#
#    for test_val,correct_val in zip(val,cor):
#        if str(test_val) != correct_val:
#            print("Test Failed")
#            print(f"{test_val} should show as {correct_val}")
#            ctr += 1
#
#    print(f"{ctr} MVPoly Tests Failed")

atom_tests()
particle_tests()

#print()
#X = (a*a+a*b) * (a-c)
#print(X)
#print(X.eval({"a":2,"b":1,"c":3}))
#print(X.reduce({"a":2}))
#print(X.reduce({"a":2,"c":3}))