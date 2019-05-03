def pairs(m=0):
    ctr = m
    while True:
        for i in range(m,ctr+1):
            yield (i,ctr)
        ctr += 1

ctr = 0 
for i in pairs(1):
    print(i)
    ctr += 1
    if ctr > 15:
        break