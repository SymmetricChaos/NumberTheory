def factorials():
    ctr = 1
    out = 1
    while True:
        out = out * ctr
        ctr += 1
        yield out
