def flatten(L):
    """Turn a list of iterables and non-iterables into a single list of their elements"""
    flat = []
    for sublist in L:
        try: 
            iter(sublist)
        except TypeError:
            flat.append(sublist)
        else:
            for item in sublist:
                flat.append(item)
    return flat


def equal_spacing(L,w,justify="right"):
    """Print a single string with the elements of the list spaced out"""
    s = ""
    if justify == "right" or justify == "r":
        for i in L:
            s += f"{i:>{w}}"
    elif justify == "left" or justify == "l":
        for i in L:
            s += f"{i:<{w}}"
    else:
        raise Exception("Justify must be left or right.")
    print(s)


def equal_spacing_grid(L,w,justify="right"):
    """Print a list of iterables into a grid"""
    for r in L:
        equal_spacing(r,w,justify)
        
        
def lists_to_tuples(*args):
    """Convert lists to a list of tuples"""
    L = []
    for i in zip(*args):
        L.append(i)
    return L


def tuples_to_lists(L):
    """Convert a list of tuples to lists"""
    out = []
    W = len(L[0])
    for w in range(W):
        out.append( [i[w] for i in L] )
    return out