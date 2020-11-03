from Sequences.Manipulations import sequence_slice, segment, offset, skips, \
                                    chunk_by_n, prepend, sequence_apply, \
                                    interleave, partial_sums, partial_prods, \
                                    make_triangle, triangle_sums, triangle_products, \
                                    binomial_transform, convolution, pairwise_sum, \
                                    pairwise_prod, pairwise_apply, differences, \
                                    hypersequence, run_length_encoding, run_lengths, \
                                    n_rep_a

from Sequences.Aliquot import aliquot, abundant, deficient, perfect, aliquot_recurrence, \
                              abundance, deficiency, untouchable, pseudoperfect, \
                              weird, highly_abundant, superabundant, amicable_pairs, \
                              practical, primitive_abundant_1, primitive_abundant_2

from Sequences.BaseDependent import evil, odious, binary_weight, co_binary_weight, \
                                    ruler, binary_length, base_length, digital_sums, \
                                    digital_roots, fraction_period, palindrome, \
                                    digital_prods, additive_persistence, multiplicative_persistence

from Sequences.BinarySequences import thue_morse, co_thue_morse

from Sequences.Collatz import collatz_length, collatz_longest, collatz_sequence, \
                              collatz_map, collatz_all, collatz_highpoint, \
                              collatz_highwater, reduced_collatz_sequence, reduced_collatz_map

from Sequences.Combinatorics import catalan, derangement, pascal, partition, \
                                    eulerian, bell, gould, even_permutation, \
                                    lazy_caterer, cake, multiplicative_partition, \
                                    central_binomial

from Sequences.Constant import pi_digits, sqrt_digits, root_digits, phi_digits, \
                               champernowne_digits, silver_ratio_digits

from Sequences.ContinuedFractions import sqrt_cfrac, e_cfrac

from Sequences.Divisibility import totients, cototients, smooth, rough, highly_composite, \
                                   divisors, prime_divisors, unique_prime_divisors, \
                                   squarefree, squarefree_kernel, coprime_characteristic, \
                                   coprimes, powerful, highly_composite_factor, \
                                   highly_composite_prime_factor, jordan_totients, \
                                   charmichael, principal_character, p_adic_order, \
                                   liouville, liouville_sums, blum, blum_blum_shub_integers, \
                                   semiprimes, almost_primes, all_divisors

from Sequences.Factorials import factorials, alternating_factorials_1, alternating_factorials_2, \
                                 kempner, double_factorials, even_double_factorials, \
                                 odd_double_factorials

from Sequences.Figurate import triangular, square, pentagonal, gen_pentagonal, \
                                polygonal, gen_polygonal, simplicial, perfect_powers, \
                                cen_polygonal, cubic, doubly_polygonal, hypercube, \
                                gen_hypercube, oblong, rectangular, square_triangular, \
                                square_pyramidal, squared_triangular

from Sequences.Fractional import numerators, denominators, harmonic, gen_harmonic, \
                                 farey, stern_brocot, dirichlet_terms, dirichlet_sums

from Sequences.Geometric import primitive_hypotenuse, nonhypotenuse, hypotenuse

from Sequences.ModularArithmetic import modular_inverses, legendre_symbols, jacobi_symbols, \
                                        kronecker_symbols, mobius_function, quadratic_residue, \
                                        quadratic_nonresidue, all_quadratic_residues, \
                                        all_quadratic_nonresidues, squares_modulo_n, \
                                        mertens_function

from Sequences.Primes import primes, primorial, prime_counting, pythagorean_primes, \
                             composites, compositorial, prime_characteristic, \
                             superprimes, noncomposite, odd_primes, twin_primes, \
                             twin_prime_pairs, prime_gaps, prime_tuples, n_gap_prime_pairs, \
                             sophie_germain_primes, safe_primes, linear_primes, congruent_primes, \
                             blum_primes

from Sequences.Pseudoprimes import fermat_pseudoprimes, weak_pseudoprimes, strong_pseudoprimes, \
                                   lucas_pseudoprimes, cipolla_pseudoprimes, fibonacci_pseudoprimes, \
                                   pell_pseudoprimes, pell_pseudoprimes_2, strong_lucas_pseudoprimes, \
                                   euler_pseudoprimes, euler_jacobi_pseudoprimes

from Sequences.Pseudorandom import LCG, ICG, CIG, aLFG, mLFG, gLFG, LFSR, middle_square, \
                                   middle_square_weyl, blum_blum_shub, lehmer, \
                                   MINSTD0, MINSTD, RANDU, shrinking_generator, \
                                   alternating_step_generator, wichmann_hill, xorshift32, \
                                   xorshift64

from Sequences.Recurrence import fibonacci, lucas, pell, companion_pell, tribonacci, \
                                 lucas_U, lucas_V, padovan, simple_recurrence, \
                                 sylvester, leonardo, arbitrary_recurrence, pisot_E, \
                                 pisot_L, pisot_P, pisot_T, ulam, perrin, semifibonacci

from Sequences.Simple import naturals, integers, arithmetic, geometric, powers, \
                             polynomial, fermat, evens, gen_evens, odds, gen_odds, \
                             counting, constant, arithmetrico_geometric, gen_polynomial, \
                             self_powers, repdigit, sign_sequence

from Sequences.Weird import recaman, nonadditive, hofstader, co_hofstader, even_odd, \
                            hofstader_Q, sierpinski, lucky





__all__=[#MANIPULATIONS
         "sequence_slice","segment","offset","skips","chunk_by_n","prepend",
         "sequence_apply","interleave","partial_sums","partial_prods",
         "make_triangle","triangle_sums","triangle_products","n_rep_a",
         "binomial_transform","convolution","pairwise_sum","pairwise_prod",
         "pairwise_apply","differences","hypersequence","run_length_encoding",
         "run_lengths",
         
         #ALIQUOT
         "aliquot","abundant","deficient","perfect","aliquot_recurrence",
         "abundance","deficiency","untouchable","pseudoperfect","weird",
         "highly_abundant","superabundant","amicable_pairs","practical",
         "primitive_abundant_1","primitive_abundant_2","amicable",
         
         #BASE DEPENDENT
         "evil","odious","binary_weight","co_binary_weight","ruler",
         "binary_length","base_length","digital_sums","digital_roots",
         "palindrome","fraction_period","digital_prods","additive_persistence",
         "multiplicative_persistence",
         
         #BINARY
         "thue_morse","co_thue_morse",
         
         #COLLATZ
         "collatz_length","collatz_longest","collatz_sequence",
         "collatz_map","collatz_all","collatz_highpoint","collatz_highwater",
         "reduced_collatz_sequence","reduced_collatz_map",
         
         #COMBINATORIC
         "catalan","derangement","pascal","partition","eulerian","bell",
         "gould","recontres","even_permutation","lazy_caterer","cake",
         "multiplicative_partition","central_binomial",
         
         #CONSTANT
         "pi_digits","sqrt_digits","root_digits","phi_digits",
         "champernowne_digits","silver_ratio_digits",
         
         #CONTINUED FRACTIONS
         "cfrac","cfrac_convergents","sqrt_cfrac","e_cfrac",
         
         #DIVISBILITY
         "totients","cototients","smooth","rough","highly_composite",
         "divisors","prime_divisors","unique_prime_divisors","squarefree",
         "squarefree_kernel","coprime_characteristic","coprimes",
         "powerful","highly_composite_factor","highly_composite_prime_factor",
         "jordan_totients","charmichael","principal_character","semiprimes",
         "p_adic_order","liouville","liouville_sums","blum","almost_primes",
         "blum_blum_shub_integers","all_divisors",
         
         #FACTORIAL
         "factorials","alternating_factorials_1","alternating_factorials_2",
         "kempner","double_factorials","even_double_factorials",
         "odd_double_factorials",
         
         #FIGURATE
         "triangular","square","pentagonal","gen_pentagonal","polygonal",
         "exponent","gen_polygonal","simplicial","perfect_powers",
         "cen_polygonal","cubic","doubly_polygonal","hypercube",
         "gen_hypercube","oblong","rectangular","square_triangular",
         "square_pyramidal","squared_triangular",
         
         #FRACTIONAL
         "numerators","denominators","harmonic","gen_harmonic","farey",
         "stern_brocot","dirichlet_terms","dirichlet_sums",
         
         #GEOMETRIC
         "primitive_hypotenuse","nonhypotenuse","hypotenuse",
         
         #MODULAR ARITHMETIC
         "modular_inverses","legendre_symbols","jacobi_symbols",
         "kronecker_symbols","mobius_function","quadratic_residue", 
         "quadratic_nonresidue","all_quadratic_residues",
         "all_quadratic_nonresidues","squares_modulo_n","mertens_function",
         
         #PRIME
         "primes","primorial","prime_counting","pythagorean_primes",
         "composites","compositorial","prime_characteristic",
         "superprimes","noncomposite","odd_primes","twin_primes",
         "twin_prime_pairs","prime_gaps","prime_tuples","n_gap_prime_pairs",
         "sophie_germain_primes","safe_primes","linear_primes",
         "congruent_primes","blum_primes",
         
         #PSEUDOPRIMES
         "fermat_pseudoprimes","weak_pseudoprimes","strong_pseudoprimes",
         "lucas_pseudoprimes","cipolla_pseudoprimes","fibonacci_pseudoprimes",
         "pell_pseudoprimes","pell_pseudoprimes_2","euler_pseudoprimes",
         "strong_lucas_pseudoprimes","euler_jacobi_pseudoprimes",
         
         #PSEUDORANDOM
         "LCG","aLFG","mLFG","gLFG","LFSR","middle_square","blum_blum_shub",
         "middle_square_weyl","ICG","CIG","lehmer","MINSTD0","MINSTD","RANDU",
         "shrinking_generator","alternating_step_generator","wichmann_hill",
         "xorshift32","xorshift64",
         
         #RECURRENCE
         "lucas","fibonacci","pell","companion_pell","tribonacci","leonardo",
         "padovan","simple_recurrence","sylvester","lucas_U","lucas_V","ulam",
         "arbitrary_recurrence","pisot_E","pisot_L","pisot_P","pisot_T",
         "perrin", "semifibonacci",
         
         #SIMPLE
         "naturals","integers","arithmetic","geometric","powers","fermat",
         "polynomial","evens","gen_evens","odds","gen_odds","counting",
         "constant","arithmetrico_geometric","gen_polynomial","self_powers",
         "repdigit","sign_sequence",
         
         #WEIRD
         "recaman","nonadditive","hofstader","co_hofstader","even_odd",
         "hofstader_Q","sierpinski","lucky",
         ]