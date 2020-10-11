## Type Errors ##
def require_integers(names,variables):
    
    out = ""
    
    for k,l in zip(names,variables):
        if type(l) != int:
            out += f"{k} must be an integer\n"
    
    if out != "":
        raise TypeError(out)


def require_callable(names,variables):
    
    out = ""
    
    for k,l in zip(names,variables):
        if not callable(l):
            out += f"{k} must be a function or other callable object\n"
    
    if out != "":
        raise TypeError(out)


def require_iterable(names,variables):
    
    out = ""
    
    for k,l in zip(names,variables):
        if not iter(l):
            out += f"{k} must be a list, tuple, generator, or other iterable object\n"
    
    if out != "":
        raise TypeError(out)


## Value Errors ##
# Following a letter by Dijkstra only "greater than or equal to" and "strictly less than" are provided
def require_geq(names,variables,n):
    
    out = ""
    
    for k,l in zip(names,variables):
        if l < n:
            out += f"{k} must be greater than or equal to {n}\n"
    
    if out != "":
        raise ValueError(out)


def require_lt(names,variables,n):
    
    out = ""
    
    for k,l in zip(names,variables):
        if l >= n:
            out += f"{k} must be strictly less than {n}\n"
    
    if out != "":
        raise ValueError(out)