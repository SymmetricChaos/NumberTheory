from NewtonsMethod import newtons_method, newtons_method_convergents
from numpy import linspace

x = 10
f0 = lambda x: 2*x**4 + 3*x**3 + 5*x + 4
f1 = lambda x: 6*x**3 + 6*x**2 + 5

for i in newtons_method_convergents(10,f0,f1):
    print(i)
    
print()
R = []
for x in linspace(-50,50,1000):
    rt = newtons_method(x,f0,f1,20)
    
    rt = rt.__round__(3)
    
    if rt not in R:
        R.append(rt)
        print(rt)