from Sequences import naturals, integers, arithmetic, geometric, powers, fibonacci, \
                      lucas, PQ_fibonacci, PQ_lucas, simple_recurrence, tribonacci, \
                      padovan, sylvesters_sequence, pell, pell_lucas, primes, \
                      primorials, smooth, rough, highly_composite, divisors, squarefree, \
                      squarefree_kernel, pythagorean_primes, triangular, square, \
                      pentagonal, gen_pentagonal, simplicial, perfect_powers, power_function, \
                      cen_polygonal, factorials, alternating_factorials, kempner_function, \
                      aliquot, abundant, deficient, perfect, derangements, catalan, \
                      pascal, partition, bell, eulerian, hypotenuse, nonhypotenuse, \
                      collatz_numbers, recaman, leonardo, fermat, prime_divisors, \
                      unique_prime_divisors, double_factorials, gould, prime_counting
                      

from Sequences.Utils import show_start

tests = [("Natural Numbers",naturals()),
         ("Integers",integers()),
         ("Arithmetic Sequence (5,3)",arithmetic(5,3)),
         ("Geometric Sequence (5,3)",geometric(5,3)),
         ("Powers of 3",powers(3)),
         ("Fibonnaci Numbers",fibonacci()),
         ("Lucas Numbers",lucas()),
         ("PQ Fibonnaci Numbers (3,2)",PQ_fibonacci(3,2)),
         ("PQ Lucas Numbers (3,2)",PQ_lucas(3,2)),
         ("Simple Recurrence (2,5)",simple_recurrence(2,5)),
         ("Tribonacci",tribonacci()),
         ("Padovan",padovan()),
         ("Sylvesters Sequence",sylvesters_sequence()),
         ("Pell Numbers",pell()),
         ("Pell-Lucas Numbers (co-Pell Numbers)",pell_lucas()),
         ("Leonardo Numbers",leonardo()),
         ("Primes",primes()),
         ("Prime Counting Functions",prime_counting()),
         ("Primorals",primorials()),
         ("5-Smooth Numbers",smooth(5)),
         ("5-Rough Numbers",rough(5)),
         ("Highly Composite Numbers",highly_composite()),
         ("Count of Divisors",divisors()),
         ("Count of Prime Divisors",prime_divisors()),
         ("Count of Unique Prime Divisors",unique_prime_divisors()),
         ("Square-Free Numbers",squarefree()),
         ("Square-Free Kernels",squarefree_kernel()),
         ("Pythagorean Primes",pythagorean_primes()),
         ("Triangular Numbers",triangular()),
         ("Square Numbers",square()),
         ("Pentagonal Numbers",pentagonal()),
         ("Generalized Pentagonal Numbers",gen_pentagonal()),
         ("Tetrahedral Numbers",simplicial(3)),
         ("Perfect Powers",perfect_powers()),
         ("Cubic Numbers",power_function(3)),
         ("Centered Triangular",cen_polygonal(3)),
         ("Factorial Numbers",factorials()),
         ("Double Factorial Numbers",double_factorials()),
         ("Alternating Factorial Numbers",alternating_factorials()),
         ("Kempner Function",kempner_function()),
         ("Aliquot Sums",aliquot()),
         ("Abundant Numbers",abundant()),
         ("Deficient Numbers",deficient()),
         ("Perfect Numbers",perfect()),
         ("Derangements",derangements()),
         ("Catalan Numbers",catalan()),
         ("Pascal's Triangle",pascal()),
         ("Gould's Sequence",gould()),
         ("Partition Numbers",partition()),
         ("Bell Numbers",bell()),
         ("Euler's Triangle",eulerian()),
         ("Hypotenuse Numbers",hypotenuse()),
         ("Nonhypotenuse Numbers",nonhypotenuse()),
         ("Collatz Numbers",collatz_numbers()),
         ("Recaman Sequence",recaman()),
         ("Fermat Numbers",fermat())
        ]

for name,seq in tests:
    print(name)
    show_start(seq)