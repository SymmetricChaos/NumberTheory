from DecimalType import Decimal

def long_multiplication_decimal(A,B):
    assert type(A) == Decimal
    assert type(B) == Decimal
    
    dA = A.digits
    dB = B.digits

    # Go through the digits of each number backward doing single digit
    # multiplication
    rows = []
    for sh,b in enumerate(reversed(dB)):
        R = [0]*(len(dA)+len(dB))
        for pos,a in enumerate(reversed(dA)):
            # Store the results of the multiplication in a row
            R[-(sh+pos)-1] = a*b
        rows.append(R)
    

    # Calculate the addition
    out = []
    carry = 0
    while len(rows[0]) > 0:
        s = carry
        for row in rows:
            s += row.pop()
        carry = s // 10
        digit = s%10
        out.append(digit)
    out.reverse()
    
    decpos = A.decpos + B.decpos
    
    w = [str(i) for i in out[:decpos]]
    f = [str(i) for i in out[decpos:]]
    d = "".join(w) + "." + "".join(f)
    
    while d[0] == "0":
        d = d[1:]
    
    print(d)
    

A = Decimal("109.12823")
B = Decimal("772.10898")
print(A)
print(B)
C = long_multiplication_decimal(A,B)
print(C)
print(109.12823*772.10898)