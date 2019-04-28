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
    """Multi bit addition via ripple method"""
    assert type(A) == Binary
    assert type(B) == Binary
    assert len(A.digits) <= w
    assert len(B.digits) <= w
       
    A = A.digits.copy()
    B = B.digits.copy()
    
    # prepend zeroes as needed
    while len(A) < w:
        A = [0] + A
    while len(B) < w:
        B = [0] + B
    
    # Show the bits of the inputs
    print("".join([str(d) for d in A]))
    print("".join([str(d) for d in B]))
    
    # Perform the ripple addition of each pair of bits from right to left
    out = [0]*w
    c = 0
    for i in reversed(range(w)):
        s, c = full_adder(A[i],B[i],c)
        out[i] = s
    
    f = Binary(out)
    print(f)
    
    if c == 1:
        print("Overflow Error!")
    
    return f


A = Binary(34564)
B = Binary(22047)
C = ripple_add(A,B,16)
