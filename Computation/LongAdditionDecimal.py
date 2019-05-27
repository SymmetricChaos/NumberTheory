def long_addition_decimal(A,B):
    assert type(A) == str
    assert type(B) == str
    
    
    # Prep the strings to be the same length on either side of the decimal
    if "." not in A:
        A = A + "."
    if "." not in B:
        B = B + "."
    
    while A.index(".") < B.index("."):
        A = "0" + A
        
    while B.index(".") < A.index("."):
        B = "0" + B
    
    while len(A)-A.index(".") < len(B)-B.index("."):
        A = A + "0"
    
    while len(B)-B.index(".") < len(A)-A.index("."):
        B = B + "0"

    
    decpos = A.index(".")
        
    # Get the digits in reverse order
    dA = [int(i) for i in reversed(A) if i != "."]
    dB = [int(i) for i in reversed(B) if i != "."]
    

    # Go through the digits of each number backward doing single digit
    # addition
    carry = 0
    out = []
    for a,b in zip(dA,dB):
        carry, digit = divmod(a+b+carry,10)
        out.append(str(digit))
    out.append(str(carry))
    
    out = "".join([i for i in reversed(out)])
    out = out[:decpos] + "." + out[decpos:]

    
    # Remove zeroes at the start and end
    while out[0] == "0":
        out = out[1:]
    while out[-1] == "0":
        out = out[:-1]
    if out[-1] == ".":
        out = out[:-1]
        
    return out

A = "4110.5"
B = "3121.5"
C = long_addition_decimal(A,B)
print(A)
print(B)
print(C)