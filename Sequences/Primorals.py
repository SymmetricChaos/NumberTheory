from Sequences import primes

def primorials(n=0, offset=0, m=0):
    
    if offset > n:
        raise Exception("Offset cannot be greater than sequence length")
    
    if n == 0:
        n = float('Inf')
    if m == 0:
        m = float('Inf')
    
    # If either one number is requested or only values less than one are 
    # requested just yield the number 1
    if n == 1 or m == 1:
        yield 1
        return None
    
    ctr = 1
    out = 1
    for i in primes():
        
        # If we passed the offset yield the value
        if ctr > offset:
            yield out
        
        # Break if we reached the iteration limit
        ctr += 1
        if ctr > n+offset:
            break
        
        out *= i
        
        # Break if we reached the maximum
        if out > m:
            break
        
    


for i in primorials(n=10,m=1000000,offset=3):
    print(i)
    
for i in primorials(n=10,m=1000000):
    print(i)
    
for num,i in enumerate(primorials(n=10)):
    print(num,i)