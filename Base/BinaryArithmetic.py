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
    
    assert type(A) == Binary
    assert type(B) == Binary
    assert len(A.digits) <= w
    assert len(B.digits) <= w
    
    A = A.digits.copy()
    B = B.digits.copy()
    
    while len(A) < w:
        A = [0] + A
    while len(B) < w:
        B = [0] + B
    
    print("".join([str(d) for d in A]))
    print("".join([str(d) for d in B]))
    
    out = []
    c = 0
    for i in range(w):
        s, c = full_adder(A[w-i-1],B[w-i-1],c)
        out.append(s)
        
    f = Binary(out[::-1])
    print(f)
    
    if c == 1:
        print("Overflow Error!")
    
    return f

    
#
#for x in [0,1]:
#    for y in [0,1]:
#        for z in [0,1]:
#            print(x,y,z,full_adder(x,y,z))

A = Binary(50880)
B = Binary(32817)
C = ripple_add(A,B,16)