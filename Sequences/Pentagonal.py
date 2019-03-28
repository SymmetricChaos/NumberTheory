def pentagonal(n=0,offset=0,m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    ctr = 0
    
    while True:
        out = (3*(ctr*ctr)-ctr)//2
        
        if out > m:
            break
        
        if ctr >= offset:
            yield out
        
        ctr += 1
        
        if ctr == n+offset:
            break

def gen_pentagonal(n=0,offset=0,m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    ctr = 0
    v = 0
    
    while True:
        out = (3*(v*v)-v)//2
        
        if out > m:
            break
        
        if ctr >= offset:
            yield out
        
        ctr += 1
        if ctr % 2 == 0:
            v -= ctr
        else:
            v += ctr
        
        if ctr == n+offset:
            break


for num,i in enumerate(pentagonal(10,1)):
    print(num,i)
    
for num,i in enumerate(gen_pentagonal(10,1)):
    print(num,i)