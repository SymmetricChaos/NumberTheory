from Sequences import naturals, fibonacci, lucas, pell, pell_lucas, tribonacci, \
                               P_fibonacci, PQ_fibonacci, padovan, integers, triangular, \
                               pentagonal, gen_pentagonal, gen_polygonal, polygonal

from Sequences.Utils import partial

for seq in [naturals, integers, fibonacci, lucas, pell, pell_lucas, tribonacci,
            padovan, triangular, pentagonal, gen_pentagonal]:
    print(seq.__doc__)
    p = partial(seq,10)
    for i in p:
        print(i)
    print()


p = partial(P_fibonacci,10,P=2)
print(P_fibonacci.__doc__)
for i in p:
    print(i)
print()

p = partial(PQ_fibonacci,num_vals=10,P=2,Q=3)
print(PQ_fibonacci.__doc__)
for i in p:
    print(i)
print()

p = partial(polygonal,num_vals=10,S=7)
print(polygonal.__doc__)
for i in p:
    print(i)
print()

p = partial(gen_polygonal,num_vals=10,S=7)
print(gen_polygonal.__doc__)
for i in p:
    print(i)
print()