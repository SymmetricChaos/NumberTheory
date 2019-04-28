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
    for r in L:
        equal_spacing(r,w,justify)
#equal_spacing([1,23,456],4,'left')
#equal_spacing([1,23,456],4,'right')
equal_spacing_grid([[1,23,456],[65,432,1]],5)