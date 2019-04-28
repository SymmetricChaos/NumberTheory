from random import randint

def add_with_carry(A,B):
    assert A < 10
    assert B < 10
    s = A+B
    return s//10, s%10

def sum_with_carry(L):
    s = sum(L)
    return s//10, s%10

def long_multiplication(A,B):
    dA = [int(i) for i in str(A)]
    dB = [int(i) for i in str(B)]
    
    rows = []
    for sh,b in enumerate(dB[::-1]):
        R = [0]*(len(dA)+len(dB))
        for pos,a in enumerate(dA[::-1]):
            R[-(sh+pos)-1] = a*b
        rows.append(R)
    
    for row in rows:
        for col in row:
            print("{:>2}".format(col),end=" ")
        print()
    
    out = ""
    carry = 0
    while len(rows[0]) > 0:
        s = carry
        for row in rows:
            s += row.pop()
        carry = s // 10
        digit = s%10
        out = str(digit) + out
    print()
    print("","  ".join([i for i in out]))
    print()
    print(int(out))
        
        
for i in range(5):
    A = randint(0,100000)
    B = randint(0,100000)
    print(A)
    print(B)
    long_multiplication(A,B)
    print("\n\n")