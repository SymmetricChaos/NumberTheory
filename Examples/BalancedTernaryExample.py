from Numerals import BalancedTernary
from random import randint

print("Balanced Ternary is an alternative way of writing numbers.")

for i in range(0,10):
    n = randint(-1000,1000)
    t = BalancedTernary(n)
    print(f"{n:4}  =  {str(t):>7} ")

print()

for i in range(0,5):
    a = BalancedTernary(randint(-200,200))
    b = BalancedTernary(randint(-200,200))
    print(f"{str(a):>6}  *  {str(b):>6}  =  {a*b}")
    
print()

for i in range(0,5):
    a = BalancedTernary(randint(-200,200))
    b = BalancedTernary(randint(-200,200))
    print(f"{str(a):>6}  +  {str(b):>6}  =  {a+b}")