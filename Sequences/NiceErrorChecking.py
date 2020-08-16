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
        raise ValueError(out)


def require_positive(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if l <= 0:
            out += f"{k} must be positive\n"
    
    if out != "":
        raise ValueError(out)


def require_geq(K,L,n):
    
    out = ""
    
    for k,l in zip(K,L):
        if l < n:
            out += f"{k} must be greater than or equal to {n}\n"
    
    if out != "":
        raise ValueError(out)


def require_leq(K,L,n):
    
    out = ""
    
    for k,l in zip(K,L):
        if l > n:
            out += f"{k} must be less than or equal to {n}\n"
    
    if out != "":
        raise ValueError(out)