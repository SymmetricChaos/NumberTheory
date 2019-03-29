def naturals_inf():

    ctr = 0
    
    while True:
        yield ctr
        
        ctr += 1

def integers_inf():
    
    ctr = 0
    v = 0
    
    while True:
        
        yield v
        
        ctr += 1
        if ctr % 2 == 0:
            v -= ctr
        else:
            v += ctr
        