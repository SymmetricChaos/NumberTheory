# Bell numbers count the partitions of a set with n elements

def bell():
    """Bell Numbers"""
    R0 = [1]
    R1 = [1,2]
    
    while True:

        yield R0[0]
        
        R2 = [R1[-1]]
        
        for i in R1:
            R2.append(i+R2[-1])
        
        R0, R1 = R1, R2