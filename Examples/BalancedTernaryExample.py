from Numerals import BalancedTernary
from random import randint

print("Balanced Ternary is an alternative way of writing numbers.")

for i in range(0,10):
    n = randint(-1000,1000)
    t = BalancedTernary(n)
    print("{:4}  =  {:>7} ".format(n,str(t)))

print()

for i in range(0,5):
    a = BalancedTernary(randint(-200,200))
    b = BalancedTernary(randint(-200,200))
    print(f"{a} * {b} = {a*b}")