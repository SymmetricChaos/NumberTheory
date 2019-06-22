def bijective_to_int(s,b):
    N = [int(i) for i in s]
    
    pws = range(0,len(N))
    out = 0
    for d,p in zip(N,reversed(pws)):
        out += d*b**p
    print(out)
    
#def int_to_bijective(n,b):
    
    
bijective_to_int("32",3)

#class BijectiveBase