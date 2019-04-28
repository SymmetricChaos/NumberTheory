# Flatten a list
def flatten(L):
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
    s = ""
    if justify == "right":
        for i in L:
            s += f"{i:>{w}}"
    if justify == "left":
        for i in L:
            s += f"{i:<{w}}"
    else:
        raise Exception("Justify must be left or right.")
    print(s)
            
equal_spacing([1,23,456],6)