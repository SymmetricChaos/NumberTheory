
def long_division(N,D,prec=10):
    
    # N is divisible by D just return the result
    if(N % D == 0):
        return(str(N//D))
        
    # Otherwise we need to setup for doing some long division
    pos = 0
    digits = []
    m = []
    ctr = 0
    
    for ctr in range(prec):
        
        # Divide the numerator by the denominator and append the result to the
        # list of digits
        digits.append(N//D)
        
        # Multiply the remainder by ten to produce the numerator for the next step
        N = (N % D)*10

        m.append(N)

    
    # If the position for the repeating decimal is zero it means that the decimal
    # actually terminates. So we only need to write down the whole number part
    # and then the decimals
    if(pos == 0):
        x1 = str(digits[0])
        x2 = "".join(str(e) for e in digits[1:])
        out = "{}.{}".format(x1,x2)
        
    return(out)

import random
for i in range(20):
    N = random.randint(1,100)
    D = random.randint(1,100)
    Q = long_division(N,D,prec=10)
    print("{}/{} = {}".format(N,D,Q))
    print()