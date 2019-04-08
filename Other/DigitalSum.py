def digital_sum(n):
    L = [int(i) for i in str(n)]
    return sum(L)
    
def digital_root(n):
    L = [int(i) for i in str(n)]
    while len(L) > 1:
        s = sum(L)
        L = [int(i) for i in str(s)]
    return s

print(digital_root(23487987654376))