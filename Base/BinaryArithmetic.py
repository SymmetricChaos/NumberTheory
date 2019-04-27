from Base import Binary

def half_adder(a,b):
    """Single bit addition"""
    return (a+b)%2

def full_adder(a,b,c=0):
    """Single bit addition with carry"""
    s = (a+b+c)%2
    cout = a*b + (c*(a+b)%2)
    return s,cout

def ripple_add(A,B,w=8):
    assert len(A) <= w
    assert len(B) <= w
    A = A.copy()
    B = B.copy()
    while len(A) < w:
        A = [0] + A
    while len(B) < w:
        B = [0] + B
    
    
    out = []
    c = 0
    for i in range(w):
        s, c = full_adder(A[w-i-1],B[w-i-1],c)
        #print(A[i],B[i],c)
        out.append(s)
    if c == 1:
        print("Overflow Error")
    
    return Binary(out[::-1])

    
#
#for x in [0,1]:
#    for y in [0,1]:
#        for z in [0,1]:
#            print(x,y,z,full_adder(x,y,z))

A = Binary(200).digits
B = Binary(127).digits
C = ripple_add(A,B)
print(A)
print(C)
print(int(C))