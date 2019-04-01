from Other.Roots import int_root, babylonian_root
from math import sqrt, floor, isclose

for i in range(1000000):
    a = sqrt(i)
    b = babylonian_root(i)
    c = int_root(i)
    
    if not isclose(a,b):
        print("Byblonian Error With {}".format(i))
        print(a)
        print(b)
        print()
        
    if floor(a) != c:
        print("Integer Root Error With {}".format(i))
        print(a)
        print(c)
        print()