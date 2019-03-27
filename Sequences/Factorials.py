def factorials(n=0):
    if n == 0:
        ctr = 1
        out = 1
        while True:
            out = out * ctr
            ctr += 1
            yield out
    else:
        out = 1
        for i in range(1,n):
            out *= i
            yield out
