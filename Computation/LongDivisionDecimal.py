def long_division_decimal(N,D,prec=10, silent=False):
    assert type(N) == str
    assert type(D) == str
    
    if "." in N:
        decposN = len(N)-N.index(".")-1
    else:
        decposN = 0
    if "." in D:
        decposD = len(D)-D.index(".")-1
    else:
        decposD = 0
    decpos = decposN + decposD
    
    
    # Get the digits
    dN = [int(i) for i in N if i != "."]
    dD = [int(i) for i in D if i != "."]
    
    print(dN)
    print(dD)
#    
#    # N is divisible by D just return the result
#    if(N % D == 0):
#        return(str(N//D))
#        
#    # Otherwise we need to setup for doing some long division
#    pos = 0
#    digits = []
#    m = []
#    ctr = 0
#    
#    while(True):
#        
#        # Divide the numerator by the denominator and append the result to the
#        # list of digits
#        digits.append(N//D)
#        
#        # Multiply the remainder by ten to produce the numerator for the next step
#        N = (N % D)*10
#        
#        # If the numerator is one we've had before then the decimal expansion is
#        # repeating and we need to stop. Also record where the repeating decimal
#        # starts
#        if(N in m):
#            pos = m.index(N)+1
#            break
#        
#        # If the numerator is zero the expansion has terminated
#        if(N == 0):
#            break
#        
#        # If we haven't reach one of the two stopping conditions put this numerator
#        # onto the list.
#        m.append(N)
#        ctr += 1
#        if ctr > prec and silent == False:
#            print("PRECISION LIMIT REACHED")
#            break
#    
#    
#    # If the position for the repeating decimal is zero it means that the decimal
#    # actually terminates. So we only need to write down the whole number part
#    # and then the decimals
#    if(pos == 0):
#        x1 = str(digits[0])
#        x2 = "".join(str(e) for e in digits[1:])
#        out = "{}.{}".format(x1,x2)
#        
#    # Otherwise write down the whole number part, then any nonrepeating part of
#    # the decimals, then the repeating part.
#    else:
#        x1 = str(digits[0])
#        x2 = "".join(str(e) for e in digits[1:pos])
#        x3 = "".join(str(e) for e in digits[pos:])
#        out = "{}.{}({})".format(x1,x2,x3)
#    return(out)
    
long_division_decimal("1.1","2.23")
