from Sequences import naturals, fibonacci, lucas, pell, pell_lucas, tribonacci, \
                               P_fibonacci, PQ_fibonacci, padovan, integers, \
                               triangular, gen_triangular, cen_triangular, \
                               square, gen_square, cen_square, \
                               pentagonal, cen_pentagonal, gen_pentagonal, \
                               primes, primorials, simplicial

from Sequences.Utils import show_vals


for seq in [naturals, integers, 
            triangular, gen_triangular, cen_triangular,
            square, gen_square, cen_square,
            pentagonal, cen_pentagonal, gen_pentagonal,
            fibonacci, lucas, pell, pell_lucas, tribonacci, padovan, 
            primes, primorials]:
    show_vals(seq)

show_vals(simplicial,D=3)
show_vals(P_fibonacci,P=3)
show_vals(PQ_fibonacci,P=3,Q=2)