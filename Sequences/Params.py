def sequence_params(n_vals,offset,max_val):
    if type(n_vals) not int:
        raise Exception("n_vals must be an integer")
    if type(offset) not int:
        raise Exception("offset must be an integer")
    if type(max_val) not int:
        raise Exception("max_val must be an integer")
        
    if n_vals < 0:
        raise Exception("n_vals must nonnegative")
    if offset < 0:
        raise Exception("offset must nonnegative")
    if max_val < 0:
        raise Exception("max_val must nonnegative")
        
    if n_vals == 0:
        n_vals = float('inf')
        
    if max_val == 0:
        max_val = float('inf')
        
    return n_vals,offset,max_val