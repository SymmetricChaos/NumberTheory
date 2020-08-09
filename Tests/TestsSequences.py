from Sequences import naturals, integers, arithmetic, geometric, powers, fibonacci, \
                      lucas, PQ_fibonacci, PQ_lucas, simple_recurrence, tribonacci, \
                      padovan, sylvesters_sequence, pell, pell_lucas, primes, \
                      primorials, smooth, rough, highly_composite, divisors, squarefree, \
                      squarefree_kernel, pythagorean_primes, triangular, square, \
                      pentagonal, gen_pentagonal, simplicial, perfect_powers, exponent, \
                      cen_polygonal, factorials, alternating_factorials, kempner_function, \
                      aliquot, abundant, deficient, perfect, derangements, catalan, \
                      pascal, partition, bell, eulerian, hypotenuse, nonhypotenuse, \
                      collatz_numbers, recaman, leonardo
                      


from Sequences.Utils import show_start

tests = [("Natural Numbers",naturals()),
         ("Integers",integers()),
         ("Arithmetic Sequence (5,3)",arithmetic(5,3)),
         ("Geometric Sequence (5,3)",geometric(5,3)),
         ("Powers of 3",powers(3)),
         ("Fibonnaci Numbers",fibonacci()),
         ("Lucas Numbers",lucas()),
         ("PQ Fibonnaci Numbers (3,1)",PQ_fibonacci(1,3)),
         ("PQ Lucas Numbers (3,1)",PQ_lucas(1,3)),
         ("Simple Recurrence (2,5)",simple_recurrence(2,5)),
         ("Tribonacci",tribonacci()),
         ("Padovan",padovan()),
         ("Sylvesters Sequence",sylvesters_sequence()),
         ("Pell Numbers",pell()),
         ("Pell-Lucas Numbers (co-Pell Numbers)",pell_lucas()),
         ("Leonardo Numbers",leonardo()),
         ("Primes",primes()),
         ("Primorals",primorials()),
         ("5-Smooth Numbers",smooth(5)),
         ("5-Rough Numbers",rough(5)),
         ("Highly Composite Numbers",highly_composite()),
         ("Count of Divisors",divisors()),
         ("Square-Free Numbers",squarefree()),
         ("Square-Free Kernels",squarefree_kernel()),
         ("Pythagorean Primes",pythagorean_primes()),
         ("Triangular Numbers",triangular()),
         ("Square Numbers",square()),
         ("Pentagonal Numbers",pentagonal()),
         ("Generalized Pentagonal Numbers",gen_pentagonal()),
         ("Tetrahedral Numbers",simplicial(3)),
         ("Perfect Powers",perfect_powers()),
         ("Cubic Numbers",exponent(3)),
         ("Centered Triangular",cen_polygonal(3)),
         ("Factorial Numbers",factorials()),
         ("Alternating Factorial Numbers",alternating_factorials()),
         ("Kempner Function",kempner_function()),
         ("Aliquot Sums",aliquot()),
         ("Abundant Numbers",abundant()),
         ("Deficient Numbers",deficient()),
         ("Perfect Numbers",perfect()),
         ("Derangements",derangements()),
         ("Catalan Numbers",catalan()),
         ("Pascal's Triangle",pascal()),
         ("Partition Numbers",partition()),
         ("Bell Numbers",bell()),
         ("Euler's Triangle",eulerian()),
         ("Hypotenuse Numbers",hypotenuse()),
         ("Nonhypotenuse Numbers",nonhypotenuse()),
         ("Collatz Numbers",collatz_numbers()),
         ("Recaman Sequence",recaman()),
          ]

for name,seq in tests:
    print(name)
    show_start(seq)