def naturals(n=0,offset=0,m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    ctr = 0
    
    while True:
        if ctr >= offset:
            yield ctr
        
        ctr += 1
        
        if ctr > m:
            break
        
        if ctr == n+offset:
            break

def integers(n=0,offset=0,m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    ctr = 0
    v = 0
    
    while True:
        
        if v > m:
            break
        
        if ctr >= offset:
            yield v
        
        ctr += 1
        if ctr % 2 == 0:
            v -= ctr
        else:
            v += ctr
        
        if ctr == n+offset:
            break

for i in naturals(20):
    print(i)
for i in integers(20):
    print(i)