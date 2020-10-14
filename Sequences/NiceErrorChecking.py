from MathUtils import miller_rabin_test
import warnings

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


def require_true(names,variables,func,description):
    
    out = ""
    
    for k,l in zip(names,variables):
        if not func(l):
            out += f"{k} {description}\n"
    
    if out != "":
        raise TypeError(out)


def require_prime(names,variables):
    
    out = ""
    
    for k,l in zip(names,variables):
        F = miller_rabin_test(l)
        if F == 0:
            out += f"{k} is not prime\n"
        if F == 2:
            prp = f"{k} is greater than 2^81 and is only probably prime"
            warnings.warn(prp)
    
    if out != "":
        raise TypeError(out)
    
    return True





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