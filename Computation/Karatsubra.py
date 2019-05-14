
def karatsuba_multiplication(A,B,m):
    
    f = 10**m
    
    x0, x1 = divmod(A,f)
    y0, y1 = divmod(B,f)
    print(x0,x1)
    print(y0,y1)

    
#    z0 = 
#    z1 = 
#    z2 = 
    
karatsuba_multiplication(12345,456789,4)