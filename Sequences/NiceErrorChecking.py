def require_integers(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if type(l) != int:
            out += f"{k} must be an integer\n"
    
    if out != "":
        raise TypeError(out)


def require_nonnegative(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if l < 0:
            out += f"{k} must be non-negative\n"
    
    if out != "":
        raise TypeError(out)


def require_positive(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if l <= 0:
            out += f"{k} must be positive\n"
    
    if out != "":
        raise TypeError(out)