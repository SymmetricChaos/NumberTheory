from Sequences.Naturals import naturals_inf, integers_inf

def polygonal_inf(S):
    
    for n in naturals_inf():
        
        yield ( n**2*(S-2)-n*(S-4) ) // 2

        
def triangular_inf():
    
    out = 0
    
    for n in naturals_inf():
        
        yield out
        
        out += n

def pentagonal_inf():
    
    for n in naturals_inf():
        out = (3*(n*n)-n)//2
        
        yield out
        

def gen_pentagonal_inf():
    
    for z in integers_inf():
        out = (3*(z*z)-z)//2
        
        yield out