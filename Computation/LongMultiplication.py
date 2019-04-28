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
    
    # Show the rows
    for row in rows:
        #print("  ",end="")
        for col in row:
            print("{:>2}".format(col),end=" ")
        print()
    
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
        
    print()
    print("","  ".join([i for i in out]))
    print()
    return int(out)
        
    
from random import randint    
for i in range(5):
    A = randint(0,20000)
    B = randint(0,A)
    print(f"{A:>7}")
    print(f"x{B:>6}\n\n")
    C = long_multiplication(A,B)
    if C != A*B:
        print("ERROR")
    print("\n\n")