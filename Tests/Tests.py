from Sequences import naturals, fibonacci, lucas, pell, pell_lucas, tribonacci, \
                               P_fibonacci, PQ_fibonacci, padovan, integers, triangular, \
                               pentagonal, gen_pentagonal, gen_polygonal, polygonal,\
                               primes, primorials, simplicial, cen_polygonal

from Sequences.Utils import show_vals





for seq in [naturals, integers, fibonacci, lucas, pell, pell_lucas, tribonacci,
            padovan, triangular, pentagonal, gen_pentagonal, primes, primorials]:
    show_vals(seq)

show_vals(simplicial,D=3)
show_vals(P_fibonacci,P=3)
show_vals(PQ_fibonacci,P=3,Q=2)
show_vals(polygonal,S=7)
show_vals(cen_polygonal,S=7)
show_vals(gen_polygonal,S=7)