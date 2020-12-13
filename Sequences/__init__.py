from Sequences.Manipulations import sequence_slice, segment, offset, skips, \
       chunk_by_n, prepend, sequence_apply, interleave, partial_sums, \
       partial_prods, make_triangle, triangle_sums, triangle_products, \
       binomial_transform, convolution, pairwise_sum, pairwise_prod, \
       pairwise_apply, differences, hypersequence, run_length_encoding, \
       run_lengths, n_rep_a

from Sequences.BaseDependent import evil, odious, binary_weight, \
       co_binary_weight, ruler, binary_length, base_length, digital_sums, \
       digital_roots, fraction_period, palindrome, digital_prods, \
       additive_persistence, multiplicative_persistence, radix_digits, \
       palindrome_digits, radix_k_weight, roman_numerals_str, roman_numerals, \
       repdigit, all_repdigit

from Sequences.BinarySequences import thue_morse, gray_codes, fibonacci_word, \
       fibonacci_words, cantor_set, paperfolding_word, paperfolding_words, \
       thue_morse_words, sierpinski_triangle

from Sequences.Cellular import rule_30, rule_30_str, rule_30_black, \
       rule_30_white, rule_90, rule_90_str, rule_90_black, rule_90_white, \
       rule_110, rule_110_str, rule_110_black, rule_110_white

from Sequences.Collatz import collatz_length, collatz_longest, \
       collatz_sequence, collatz_map, collatz_all, collatz_highpoint, \
       collatz_highwater, reduced_collatz_sequence, reduced_collatz_map

from Sequences.Constant import pi_digits, sqrt_digits, root_digits, \
       phi_digits, champernowne_digits, silver_ratio_digits

from Sequences.Figurate import triangular, square, pentagonal, \
       gen_pentagonal, polygonal, gen_polygonal, simplicial, perfect_powers, \
       cen_polygonal, cubic, doubly_polygonal, hypercube, gen_hypercube, \
       oblong, rectangular, square_triangular, square_pyramidal, \
       squared_triangular

from Sequences.Geometric import primitive_hypotenuse, nonhypotenuse, \
       hypotenuse, mosner, primitive_pythagorean_triples, \
       pythagorean_triples

from Sequences.ModularArithmetic import modular_inverses, legendre_symbols, \
       jacobi_symbols, kronecker_symbols, mobius_function, quadratic_residue, \
       quadratic_nonresidue, all_quadratic_residues, \
       all_quadratic_nonresidues, squares_modulo_n, mertens_function

from Sequences.Pseudorandom import LCG, ICG, CIG, aLFG, mLFG, gLFG, LFSR, \
       middle_square,  middle_square_weyl, blum_blum_shub, lehmer, MINSTD0, \
       MINSTD, RANDU, shrinking_generator, alternating_step_generator, \
       wichmann_hill, xorshift32, xorshift64

from Sequences.Recurrence import fibonacci, lucas, pell, companion_pell, \
       tribonacci, lucas_U, lucas_V, padovan, simple_recurrence, sylvester, \
       leonardo, arbitrary_recurrence, pisot_E, pisot_L, pisot_P, pisot_T, \
       ulam, perrin, semifibonacci, tribonnaci_word, tribonnaci_words, \
       narayana_cows

from Sequences.Simple import naturals, integers, arithmetic, geometric, \
      powers, polynomial, fermat, evens, gen_evens, odds, gen_odds, counting, \
      constant, arithmetrico_geometric, gen_polynomial, self_powers, \
      sign_sequence, floyd_triangle, magic_square

from Sequences.Totient import totients, cototients, charmichael, \
       jordan_totients, totient_range, nontotients, even_nontotients, \
       sparsely_totient, highly_totient, totient_count

from Sequences.Weird import recaman, nonadditive, hofstader, co_hofstader, \
       even_odd, hofstader_Q, lucky





__all__=[#MANIPULATIONS
         "sequence_slice","segment","offset","skips","chunk_by_n","prepend",
         "sequence_apply","interleave","partial_sums","partial_prods",
         "make_triangle","triangle_sums","triangle_products","n_rep_a",
         "binomial_transform","convolution","pairwise_sum","pairwise_prod",
         "pairwise_apply","differences","hypersequence","run_length_encoding",
         "run_lengths",
         
         #BASE DEPENDENT
         "evil","odious","binary_weight","co_binary_weight","ruler",
         "binary_length","base_length","digital_sums","digital_roots",
         "palindrome","fraction_period","digital_prods","additive_persistence",
         "multiplicative_persistence","radix_digits","palindrome_digits",
         "radix_k_weight","roman_numerals_str","roman_numerals","repdigit",
         "all_repdigit",
         
         #BINARY
         "thue_morse","gray_codes","fibonacci_word","fibonacci_words",
         "cantor_set","cantor_sets","paperfolding_word","paperfolding_words",
         "thue_morse_words","sierpinski_triangle",
         
         #CELLULAR
         "rule_30","rule_30_str","rule_30_black","rule_30_white","rule_90",
         "rule_90_str","rule_90_black","rule_90_white","rule_110",
         "rule_110_str","rule_110_black","rule_110_white",
         
         #COLLATZ
         "collatz_length","collatz_longest","collatz_sequence",
         "collatz_map","collatz_all","collatz_highpoint","collatz_highwater",
         "reduced_collatz_sequence","reduced_collatz_map",
         
         #CONSTANT
         "pi_digits","sqrt_digits","root_digits","phi_digits",
         "champernowne_digits","silver_ratio_digits",
         
         #FIGURATE
         "triangular","square","pentagonal","gen_pentagonal","polygonal",
         "exponent","gen_polygonal","simplicial","perfect_powers",
         "cen_polygonal","cubic","doubly_polygonal","hypercube",
         "gen_hypercube","oblong","rectangular","square_triangular",
         "square_pyramidal","squared_triangular",
         
         #GEOMETRIC
         "primitive_hypotenuse","nonhypotenuse","hypotenuse","mosner",
         "primitive_pythagorean_triples","pythagorean_triples",
         
         #MODULAR ARITHMETIC
         "modular_inverses","legendre_symbols","jacobi_symbols",
         "kronecker_symbols","mobius_function","quadratic_residue", 
         "quadratic_nonresidue","all_quadratic_residues",
         "all_quadratic_nonresidues","squares_modulo_n","mertens_function",
         
         #PSEUDORANDOM
         "LCG","aLFG","mLFG","gLFG","LFSR","middle_square","blum_blum_shub",
         "middle_square_weyl","ICG","CIG","lehmer","MINSTD0","MINSTD","RANDU",
         "shrinking_generator","alternating_step_generator","wichmann_hill",
         "xorshift32","xorshift64",
         
         #RECURRENCE
         "lucas","fibonacci","pell","companion_pell","tribonacci","leonardo",
         "padovan","simple_recurrence","sylvester","lucas_U","lucas_V","ulam",
         "arbitrary_recurrence","pisot_E","pisot_L","pisot_P","pisot_T",
         "perrin", "semifibonacci","tribonnaci_word","tribonnaci_words",
         "narayana_cows",
         
         #SIMPLE
         "naturals","integers","arithmetic","geometric","powers","fermat",
         "polynomial","evens","gen_evens","odds","gen_odds","counting",
         "constant","arithmetrico_geometric","gen_polynomial","self_powers",
         "sign_sequence","floyd_triangle","magic_square",
         
         #TOTIENT
         "totients","cototients","charmichael","jordan_totients",
         "totient_range","nontotients","even_nontotients","sparsely_totient",
         "highly_totient","totient_count",
         
         #WEIRD
         "recaman","nonadditive","hofstader","co_hofstader","even_odd",
         "hofstader_Q","lucky",
         ]