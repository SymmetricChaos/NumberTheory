def long_division_decimal(N,D,prec=15):
    assert type(N) == str
    assert type(D) == str
    
#    while N[0] == "0":
#        N = N[1:]
#        
#    while D[0] == "0":
#        D = D[1:]
    
    decpos = 0
    if "." in N:
        decpos += N.index(".")-1
    if "." in D:
        decpos += len(D)-D.index(".")
#        
#    print("decpos",decpos)
    
    N = [int(i) for i in N if i != "."]
    while len(N) < prec+decpos:
        N.append(0)
    D = int(D.replace(".",""))

    
    # Division of finite decimals is not a closed operation because of this we
    # need to choose a finite number of steps. In this case the entire integer
    # part is calculated and then some defined number of digits.
    digits = []
    num = N[0]
    for pos in range(prec+decpos-1):
        # Divide the numerator by the denominator and append the result to the
        # list of digits
        digits.append(num//D)
#        
#        print(num%D)
#        print(num%D*10)
        # Multiply the remainder by ten to produce the numerator for the next step
        num = (num % D)*10+N[pos+1]
#        print(num)
#        print()


    out = "".join([str(i) for i in digits])
    out = out[:decpos] + "." + out[decpos:]
    while out[0] == "0":
        out = out[1:]
        
    return out

A = "213.21"
B = "12.15"
print(A)
print(B)
print(long_division_decimal(A,B))
print(float(A)/float(B))