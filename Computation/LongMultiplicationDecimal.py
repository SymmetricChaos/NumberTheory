def long_multiplication_decimal(A,B):
    assert type(A) == str
    assert type(B) == str
    
    if "." in A:
        decposA = len(A)-A.index(".")-1
    else:
        decposA = 0
    if "." in B:
        decposB = len(B)-B.index(".")-1
    else:
        decposB = 0
    decpos = decposA + decposB
    
    A = A.replace(".","")
    B = B.replace(".","")
    
    # Get the digits
    dA = [int(i) for i in A]
    dB = [int(i) for i in B]
    
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
    out = ""
    carry = 0
    while len(rows[0]) > 0:
        s = carry
        for row in rows:
            s += row.pop()
        carry = s // 10
        digit = s%10
        out = str(digit) + out
    
    invdecpos = len(out)-decpos
    out = out[:invdecpos] + "." + out[invdecpos:]
    
    # Remove zeroes at the start and end
    while out[0] == "0":
        out = out[1:]
    while out[-1] == "0":
        out = out[:-1]
    
    return out

a = long_multiplication_decimal("109.12","2.10")
print(a)