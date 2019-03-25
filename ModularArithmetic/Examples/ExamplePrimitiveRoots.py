from ModularArithmetic import primitive_roots, coprimes, show_congruences

m = 11
r = primitive_roots(m)
print("numbers coprime to {}\n{}\n".format(m,coprimes(m)))
print("primitive roots mod {}\n{}\n".format(m,r))
for i in r:
    show_congruences(i,m)