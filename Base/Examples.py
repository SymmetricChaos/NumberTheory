from Base import BalancedTernary
from random import randint


for i in range(0,30):
    n = randint(-1000,1000)
    t = BalancedTernary(n)
    print("{:4}  =  {:>7} ".format(n,str(t)))