from Sequences.Simple import naturals

def collatz_step(n):
    if n % 2 == 1:
        return 3*n+1
    return n//2


def collatz_numbers():
    """Collatz Numbers: Time for the Collatz Function to reach zero when starting at each positive integer"""
    
    D = {1 : 0, 2 : 1, 4 : 2}
    

    for n in naturals(1):
        if n in D:
            yield D[n]
        
        else:
            ctr = n
            length = 0
            
            while ctr not in D:
                ctr = collatz_step(ctr)
                length += 1
            
            D[n] = D[ctr] + length
            yield D[n]