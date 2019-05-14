
def karatsuba_multiplication(A,B,m):
    
    f1 = 10**m
    f2 = f1*f1
    
    x0, x1 = divmod(A,f1)
    y0, y1 = divmod(B,f1)
    print(x0,x1)
    print(y0,y1)

    
    z0 = x0*y0
    z2 = x1*y1
    z1 = (x1+x0)*(y1+y0)-z2-z0
    
    print(f"{z0} * {f2} + {z1} * {f1} + {z2}")
    print(z0*f2 + z1*f1 + z2)
    
    print(A*B)
    
karatsuba_multiplication(12345,6789,3)