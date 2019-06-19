from Numerals import factoradic

print("The factoradic numbers are an unusual way of represent numbers. Usuaully numeral systems have place values that increase by powers of some integer. Factoradic numbers have place values that are successive factorials.")

print("\nWe can write 67 as:")

print(factoradic(67))

print("Because:")

print("4! * 2 + 3! * 3 + 2! * 0 + 1! * 1 + 0! * 0")
print("24*2 + 6*3 + 2*0 + 1*1 + 1*0")
print("48 + 18 + 0 + 1 + 0")
print("67")

print("\nBesides being an interesting concept factoradics are useful in working with permutations.")

def factoradic_permutation(L,f):
    
    F = factoradic(f)
    out = []
    while len(L) > len(F):
        out.append( L.pop(0) )
    for i in F:
        out.append( L.pop(i) ) 
    return out


for i in range(24):
    L = ["A","B","C","D"]
    print("".join(factoradic_permutation(L,i)), factoradic(i))