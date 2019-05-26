def long_division_decimal(N,D,prec=15, silent=False):
    assert type(N) == str
    assert type(D) == str
    
    if "." in N:
        decposN = N.index(".")
    else:
        decposN = 0
    if "." in D:
        decposD = D.index(".")
    else:
        decposD = 0
    decpos = decposN + decposD
    
    D = int(D.replace(".",""))
    N = [int(i) for i in N if i != "."]
    while len(N) < prec:
        N.append(0)
    
    print()
    print(N)
    print(D)
    print()
    # Setup for doing some long division
    digits = []
    num = N[0]
    for pos in range(prec-1):
        # Divide the numerator by the denominator and append the result to the
        # list of digits
        digits.append(num//D)
        
        # Multiply the remainder by ten to produce the numerator for the next step
        num = (num % D)*10+N[pos+1]
        

    out = "".join([str(i) for i in digits])
    out = out[:decpos] + "." + out[decpos:]
#    while out[0] == "0":
#        out = out[1:]
        
    return out

A = "213.21"
B = "1.1"
print(A)
print(B)
print(long_division_decimal(A,B))
print(213.21/1.1)