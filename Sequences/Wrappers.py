from Sequences.Utils import sequence_maker
from Sequences.Naturals import naturals_inf
from Sequences.Recurrence import fibonacci_inf, lucas_inf, pell_inf, pell_lucas_inf,\
                                 tribonacci_inf, P_fibonacci_inf, PQ_fibonacci_inf,\
                                 padovan_inf

naturals = sequence_maker(naturals_inf)
fibonacci = sequence_maker(fibonacci_inf)
lucas = sequence_maker(lucas_inf)
pell = sequence_maker(pell_inf)
pell_lucas = sequence_maker(pell_lucas_inf)
tribonacci = sequence_maker(tribonacci_inf)
P_fibonacci = sequence_maker(P_fibonacci_inf)
PQ_fibonacci = sequence_maker(PQ_fibonacci_inf)
padovan = sequence_maker(padovan_inf)