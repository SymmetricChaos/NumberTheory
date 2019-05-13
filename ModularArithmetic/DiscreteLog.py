# The discrete log is only guaranteed t exist when b is a primitive root of m
# (ie when it is a generator)

def discrete_log(x,b,m):
    """integer k such that b^k = x (mod m)"""
    if x == 1:
        return 0
    t = 1
    for k in range(1,m):
        # To save some work we multiply by b at each step rather than
        # going to the trouble of calculating b^k each time
        t = (t*b) % m
        if t == x:
            return k
    
print(discrete_log(5,24,31))
