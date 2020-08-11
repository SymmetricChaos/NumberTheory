def require_integers(K,L):
    
    out = ""
    
    for k,l in zip(K,L):
        if type(l) != int:
            out += f"{k} must be an integer\n"
    
    if out != "":
        raise TypeError(out)