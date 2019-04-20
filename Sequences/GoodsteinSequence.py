import parser

def baseConvert(n,b):
    if b < 1:
        return []
    if b == 1:
        return [1]*n
    if(n == 0):
        return([0])
    out = []
    while(n > 0):
        out.append(n%b)
        n //= b
    return(out[::-1])
    
## Calculate a single level of hereditary base notation.
def hered_base_level(n,b):
    A = baseConvert(n,b)
    E = [i for i in range(len(A))]
    E = E[::-1]
    S = ""
    for i in range(len(A)):
        
        ## If the coefficient is zero ignore this term entirely
        if A[i] == 0:
            continue
        
        ## For the exponent 0 we only want to coefficient
        if E[i] == 0:
            S += "{}".format(A[i])
            continue
        
        ## For the exponent 1 we only want the coefficient and base
        if E[i] == 1:
            if A[i] != 0 and A[i] != 1:
                S += "{}*{}".format(A[i],b)
            if A[i] == 1:
                S += "{}".format(b)
            S += " + "
            continue
        
        ## For most exponents we need the coefficient, base, and exponent
        ## In order to find the exponent when calculting the full hereditary
        ## base representation we surround it with square brackets
        if i < len(A)-2:
            if A[i] != 0 and A[i] != 1:
                S += "{}*{}^[{}]".format(A[i],b,E[i])
            if A[i] == 1:
                S += "{}^[{}]".format(b,E[i])
            S += " + "

    ## Detect and remove any trailing " + "
    if S[-1] == " ":
        S = S[:-3]
    return S

## Find the position of the square brackets and return everything between them
def findExps(s):
    start1 = 0
    start2 = 0
    r = s.count("[")
    for i in range(r):
        start1 = s.find("[",start1)
        start2 = s.find("]",start2)
        yield s[start1+1:start2]
        start1 += 1
        start2 += 1


## The complete hereditary base function
def hered_base(n,b):
    ## Calculate the first level
    S = hered_base_level(n,b)
    ## Keep checking the string to see if we need to replace any of the
    ## exponents. Whenever we do switch brackets for parentheses.
    while True:
        ctr = 0
        for i in findExps(S):
            if int(i) > b:
                t = hered_base_level(int(i),b)
                t = t.replace(" ","")
                S = S.replace("["+i+"]","("+t+")")
                ctr += 1
        ## If there is nothing to replace strip out the square brackets, check
        ## that we did it right and return the string.
        if ctr == 0:
            S = S.replace("[","")
            S = S.replace("]","")
            if hered_to_dec(S) != n:
                print("ERROR")
            return S

## This function converts the notation to standard Python then interprets it
## into an integer. We use this both to check our work and calculate the
## Goodstein sequence
def hered_to_dec(s):
    s = s.replace("^","**")
    code = parser.expr(s).compile()
    return eval(code)

## Calculate the Goodstein sequence for n out to x terms
def goodstein_sequence(n):
    """Goodstein Sequence"""
    yield n
    t = n
    ctr = 1
    while True:
        ctr += 1
        H = hered_base(t,ctr)
        H = H.replace(str(ctr),str(ctr+1))
        H += " - 1"
        t = hered_to_dec(H)
        yield t

# import random
#print("Examples of Hereditary Base-3 Notation")
#for i in range(9):
#    t = random.randint(10,1000)
#    H = heredbase(t,3)
#    print("{:<3}  =  {}".format(t,H))
#print("\n")


#for X in range(4,17):
#    print("Goodstein Sequence")
#    for b,i in enumerate(goodstein_sequence(X)):
#        if b > 10:
#            break
#        print(i)
#        #print("{:<5}    = {}".format(i,hered_base(i,b+2)))