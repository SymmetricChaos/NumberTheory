from GeneralUtils import equal_spacing, equal_spacing_grid

def long_multiplication(A,B):
    # Get the digits
    dA = [int(i) for i in str(A)]
    dB = [int(i) for i in str(B)]
    
    # Go through the digits of each number backward doing single digit
    # multiplication
    rows = []
    for sh,b in enumerate(reversed(dB)):
        R = [0]*(len(dA)+len(dB))
        for pos,a in enumerate(reversed(dA)):
            # Store the results of the multiplication in a row
            R[-(sh+pos)-1] = a*b
        rows.append(R)
    
    equal_spacing_grid(rows,3)

    # Calculate the addition and
    
    out = ""
    carry = 0
    C = []
    while len(rows[0]) > 0:
        C.append(carry)
        s = carry
        for row in rows:
            s += row.pop()
        carry = s // 10
        digit = s%10
        out = str(digit) + out
    
    equal_spacing(reversed(C),3)
    
    print()
    equal_spacing(out,3)
    
    return int(out)
        