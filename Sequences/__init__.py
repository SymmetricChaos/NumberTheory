from Sequences.Manipulations import sequence_slice, segment, offset, skips, \
                                    chunk_by_n, prepend, sequence_apply, \
                                    interleave, partial_sums, partial_prods, \
                                    make_triangle, triangle_sums, triangle_products, \
                                    binomial_transform, convolution, pairwise_sum, \
                                    pairwise_prod, pairwise_apply, differences, \
                                    hypersequence, run_length_encoding, run_lengths, \
                                    n_rep_a

from Sequences.Recurrence import fibonacci, lucas, pell, companion_pell, tribonacci, \
                                 lucas_U, lucas_V, padovan, simple_recurrence, \
                                 sylvester, leonardo, arbitrary_recurrence, pisot_E, \
                                 pisot_L, pisot_P, pisot_T, ulam, perrin, semifibonacci

from Sequences.Polygonal import triangular, square, pentagonal, gen_pentagonal, \
                                polygonal, gen_polygonal, simplicial, perfect_powers, \
                                cen_polygonal, cubic, doubly_polygonal, hypercube, \
                                gen_hypercube, oblong, rectangular, square_triangular, \
                                square_pyramidal, squared_triangular

from Sequences.Simple import naturals, integers, arithmetic, geometric, powers, \
                             polynomial, fermat, evens, gen_evens, odds, gen_odds, \
                             counting, constant, arithmetrico_geometric, gen_polynomial, \
                             self_powers, repdigit, sign_sequence

from Sequences.Primes import primes, primorial, smooth, rough, highly_composite, \
                             divisors, squarefree, squarefree_kernel, prime_counting, \
                             pythagorean_primes, unique_prime_divisors, prime_divisors, \
                             composites, totients, compositorial, prime_characteristic, \
                             coprime_characteristic, cototients, superprimes, lucky, \
                             noncomposite, odd_primes, twin_primes, \
                             cousin_primes, sexy_primes, prime_gaps, powerful

from Sequences.Factorials import factorials, alternating_factorials_1, alternating_factorials_2, \
                                 kempner, double_factorials, even_double_factorials, \
                                 odd_double_factorials

from Sequences.Aliquot import aliquot, abundant, deficient, perfect, aliquot_recurrence, \
                              abundance, deficiency, untouchable, pseudoperfect, \
                              weird, highly_abundant, superabundant, amicable_pairs, \
                              practical, primitive_abundant_1, primitive_abundant_2

from Sequences.Combinatorics import catalan, derangement, pascal, partition, \
                                    eulerian, bell, gould, even_permutation, \
                                    lazy_caterer, cake, multiplicative_partition, \
                                    central_binomial

from Sequences.ContinuedFractions import sqrt_cfrac, e_cfrac

from Sequences.Geometric import primitive_hypotenuse, nonhypotenuse, hypotenuse

from Sequences.BinarySequences import thue_morse, co_thue_morse

from Sequences.Pseudorandom import LCG, LFG, LFSR

from Sequences.Collatz import collatz_length, collatz_longest, collatz_sequence, \
                              collatz_map, collatz_all, collatz_highpoint, \
                              collatz_highwater, reduced_collatz_sequence, reduced_collatz_map

from Sequences.Weird import recaman, nonadditive, hofstader, co_hofstader, even_odd

from Sequences.BaseDependent import evil, odious, binary_weight, co_binary_weight, \
                                    ruler, binary_length, base_length, digital_sums, \
                                    digital_roots, fraction_period, palindrome, \
                                    digital_prods, additive_persistence, multiplicative_persistence

from Sequences.Constant import pi_digits, sqrt_digits, root_digits, phi_digits, \
                               champernowne_digits, silver_ratio_digits

from Sequences.Fractional import numerators, denominators, harmonic, gen_harmonic, \
                                 farey, stern_brocot

from Sequences.ModularArithmetic import modular_inverses, legendre_symbols, jacobi_symbols, \
                                        mobius_function

__all__=[#MANIPS
         "sequence_slice","segment","offset","skips","chunk_by_n","prepend",
         "sequence_apply","interleave","partial_sums","partial_prods",
         "make_triangle","triangle_sums","triangle_products",
         "binomial_transform","convolution","pairwise_sum","pairwise_prod",
         "pairwise_apply","differences","hypersequence","run_length_encoding",
         "run_lengths","n_rep_a",
         
         #RECURRENCE
         "lucas","fibonacci","pell","companion_pell","tribonacci","leonardo",
         "padovan","simple_recurrence","sylvester","lucas_U","lucas_V","ulam",
         "arbitrary_recurrence","pisot_E","pisot_L","pisot_P","pisot_T",
         "perrin", "semifibonacci",
         
         #POLYGONAL
         "triangular","square","pentagonal","gen_pentagonal","polygonal",
         "exponent","gen_polygonal","simplicial","perfect_powers",
         "cen_polygonal","cubic","doubly_polygonal","hypercube",
         "gen_hypercube","oblong","rectangular","square_triangular",
         "square_pyramidal","squared_triangular",
         
         #SIMPLE
         "naturals","integers","arithmetic","geometric","powers","fermat",
         "polynomial","evens","gen_evens","odds","gen_odds","counting",
         "constant","arithmetrico_geometric","gen_polynomial","self_powers",
         "repdigit","sign_sequence",
         
         #PRIME
         "primes","primorial","smooth","rough","highly_composite", "divisors",
         "squarefree","squarefree_kernel","pythagorean_primes","lucky",
         "prime_counting","prime_divisors","unique_prime_divisors",
         "composites","totients","compositorial","hamming","cototients",
         "prime_characteristic","coprime_characteristic","superprimes",
         "noncomposite","mobius_function","odd_primes","twin_primes",
         "cousin_primes","sexy_primes","prime_gaps","powerful",
         
         #FACTORIAL
         "factorials","alternating_factorials_1","alternating_factorials_2",
         "kempner","double_factorials","even_double_factorials",
         "odd_double_factorials",
         
         #ALIQUOT
         "aliquot","abundant","deficient","perfect","aliquot_recurrence",
         "abundance","deficiency","untouchable","pseudoperfect","weird",
         "highly_abundant","superabundant","amicable_pairs","practical",
         "primitive_abundant_1","primitive_abundant_2",
         
         #COMBINATORIC
         "catalan","derangement","pascal","partition","eulerian","bell",
         "gould","recontres","even_permutation","lazy_caterer","cake",
         "multiplicative_partition","central_binomial",
         
         #CONTINUED FRACTIONS
         "cfrac","cfrac_convergents","sqrt_cfrac","e_cfrac",
         
         #GEOMETRIC
         "primitive_hypotenuse","nonhypotenuse","hypotenuse",
         
         #BINARY
         "thue_morse","co_thue_morse",
         
         #PRNG
         "LCG","LFG","LFSR",
         
         #COLLATZ
         "collatz_length","collatz_longest","collatz_sequence",
         "collatz_map","collatz_all","collatz_highpoint","collatz_highwater",
         "reduced_collatz_sequence","reduced_collatz_map",
         
         #WEIRD
         "recaman","nonadditive","hofstader","co_hofstader","even_odd",
         
         #BASE DEPENDENT
         "evil","odious","binary_weight","co_binary_weight","ruler",
         "binary_length","base_length","digital_sums","digital_roots",
         "palindrome","fraction_period","digital_prods","additive_persistence",
         "multiplicative_persistence",
         
         #CONSTANT
         "pi_digits","sqrt_digits","root_digits","phi_digits",
         "champernowne_digits","silver_ratio_digits",
         
         #FRACTIONAL
         "numerators","denominators","harmonic","gen_harmonic","farey",
         "stern_brocot",
        ]