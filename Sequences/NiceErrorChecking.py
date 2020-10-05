## Type Errors ##
def require_integers(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if type(l) != int:
            out += f"{k} must be an integer\n"
    
    if out != "":
        raise TypeError(out)


def require_callable(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if not callable(l):
            out += f"{k} must be a function or other callable object\n"
    
    if out != "":
        raise TypeError(out)


def require_iterable(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if not iter(l):
            out += f"{k} must be a list, tuple, generator, or other iterable object\n"
    
    if out != "":
        raise TypeError(out)


## Value Errors ##
# Following a letter by Dijkstra only "greater than or equal to" and "strictly less than" are provided
def require_geq(K,L,n):
    
    out = ""
    
    for k,l in zip(K,L):
        if l < n:
            out += f"{k} must be greater than or equal to {n}\n"
    
    if out != "":
        raise ValueError(out)


def require_lt(K,L,n):
    
    out = ""
    
    for k,l in zip(K,L):
        if l >= n:
            out += f"{k} must be strictly less than {n}\n"
    
    if out != "":
        raise ValueError(out)