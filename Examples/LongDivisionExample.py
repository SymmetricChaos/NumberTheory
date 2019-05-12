def long_division_steps(N,D,prec=10):
    
    print(f"Steps of dividing {N} by {D}\n")
    
    if(N % D == 0):
        return(str(N//D))
    
    pos = 0
    digits = []
    m = []
    
    w1 = len(str(N))+1
    w2 = len(str(D))
    
    while(True):
        print(f"{N:<{w1}} / {D:<{w2}}  =  {N//D} R {N%D}")

        digits.append(N//D)
        
        N = (N % D)*10
        
        if(N in m):
            pos = m.index(N)+1
            break
        
        if(N == 0):
            break
        
        m.append(N)
    print()

    if(pos == 0):
        x1 = str(digits[0])
        x2 = "".join(str(e) for e in digits[1:])
        out = "{}.{}".format(x1,x2)
        
    else:
        x1 = str(digits[0])
        x2 = "".join(str(e) for e in digits[1:pos])
        x3 = "".join(str(e) for e in digits[pos:])
        out = "{}.{}({})".format(x1,x2,x3)
    return(out)

N = int(input("Numerator:   "))
D = int(input("Denominator: "))
print()
#import random
#N = random.randint(1,1000)
#D = random.randint(1,1000)
Q = long_division_steps(N,D,prec=10)
print(f"{N} / {D} = {Q}")
print()