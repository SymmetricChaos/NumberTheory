from Sequences.Utils import sequence
from Sequences.Naturals import naturals_inf, integers_inf
from Sequences.Recurrence import fibonacci_inf, lucas_inf, pell_inf, pell_lucas_inf,\
                                 tribonacci_inf, P_fibonacci_inf, PQ_fibonacci_inf,\
                                 padovan_inf
from Sequences.Polygonal import polygonal_inf, triangular_inf, pentagonal_inf, \
                                gen_pentagonal_inf

# Very simple sequences
naturals = sequence(naturals_inf)
integers = sequence(integers_inf)

# Reccurence relations
fibonacci = sequence(fibonacci_inf)
lucas = sequence(lucas_inf)
pell = sequence(pell_inf)
pell_lucas = sequence(pell_lucas_inf)
tribonacci = sequence(tribonacci_inf)
P_fibonacci = sequence(P_fibonacci_inf)
PQ_fibonacci = sequence(PQ_fibonacci_inf)
padovan = sequence(padovan_inf)

# Polygonal numbers
polygonal = sequence(polygonal_inf)
triangular = sequence(triangular_inf)
pentagonal = sequence(pentagonal_inf)
gen_pentagonal = sequence(gen_pentagonal_inf)