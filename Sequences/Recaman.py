def recaman():
    """Recaman Sequence"""
    used = [0]
    ctr = 0
    while True:
        yield used[-1]
        ctr += 1
        cur = used[-1]
        
        if cur - ctr < 0:
            used.append(cur+ctr)
            continue
        if cur - ctr in used:
            used.append(cur+ctr)
            continue
        else:
            used.append(cur-ctr)