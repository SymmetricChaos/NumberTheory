def triangular(n=0,offset=0,m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    out = 0
    ctr = 1
    
    while True:
        
        if ctr >= offset:
            yield out
        
        out += ctr
        ctr += 1
        
        if ctr == n+offset+1:
            break
        if out > m:
            break
        
for num,i in enumerate(triangular(10,0)):
    print(num,i)