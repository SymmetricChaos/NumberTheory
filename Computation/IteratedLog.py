def iterated_log(x,b):
    if x <= 1:
        return 0
    if x <= b:
        return 1
    else:
        base = b
        ctr = 1
        while x > b:
            ctr += 1
            b = base**b
        return ctr
