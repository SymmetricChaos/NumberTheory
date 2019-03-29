def sequence_params(num_vals,offset,min_val,max_val):
    
    if type(num_vals) != int:
        raise Exception("n_vals must be an integer")
    if type(offset) != int:
        raise Exception("offset must be an integer")
    if type(min_val) != int:
        raise Exception("min_val must be an integer")
    if type(max_val) != int:
        raise Exception("max_val must be an integer")

        
    if num_vals < 0:
        raise Exception("n_vals must be nonnegative")
    if offset < 0:
        raise Exception("offset must ber nonnegative")
    if min_val < 0:
        raise Exception("min_val must be nonnegative")
    if max_val < 0:
        raise Exception("max_val must be nonnegative")

    if min_val > max_val:
        raise Exception("min_val cannot be greather than max_val")
    
    if offset > num_vals:
        raise Exception("offset cannot be greater than num_vals")
        
        
def sequence_maker(generator):
    
    def S(num_vals=0,offset=0,min_val=0,max_val=0,**kwargs):
        
        sequence_params(num_vals, offset, min_val, max_val)
    
        if max_val == 0:
            max_val = float('inf')
            
        if num_vals == 0:
            num_vals = float('inf')
            
        for ctr,val in enumerate(generator(**kwargs)):
            if ctr >= num_vals+offset or val > max_val or ctr < min_val:
                break
            
            if val >= min_val and ctr >= offset:
                yield val
                
    return S