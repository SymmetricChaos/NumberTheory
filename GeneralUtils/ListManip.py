# Flatten a list
def flatten(L):
    """Turn a list of iterable into a single list of their elements"""
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