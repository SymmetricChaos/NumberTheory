def collatz_step(n):
    if n % 2 == 1:
        return 3*n+1
    return n//2

def collatz_numbers():
    D = {1 : 0, 2 : 1, 4 : 2}
    
    n = 0
    while True:
        n += 1
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