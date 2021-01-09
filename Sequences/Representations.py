# For alternate representations, generally as strings

from Sequences.Simple import naturals
from Sequences.MathUtils import int_to_roman, int_to_name

def roman_numerals_str():
    """
    The positive integers as standard Roman Numerals, returns strings
    """
    
    for n in naturals(1):
        yield int_to_roman(n)


def roman_numerals():
    """
    The positive integers as standard Roman Numerals in numeric form\n
    OEIS A093796
    """
    
    D = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V":5, "I": 1}
    for R in roman_numerals_str():
        yield tuple([D[letter] for letter in R])


def number_names_str(hyphen=False,use_and=False,long_scale=False):
    """
    The English names of the natural numbers, returns strings
    
    Args:
        n -- int to be named
        hyphen --bool, use hyphens for numbers like forty-eight
        use_and -- bool, use the phrasing "hundred and" rather than just "hundred"
        long_scale -- bool, use the long scale where (1,000,000 = 'one thousand million')
    
    With short scale goes up to 65 digit numbers
    With long scale goes up to 122 digit numbers
    """
    
    for n in naturals():
        yield int_to_name(n,hyphen,use_and,long_scale)




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nNames of Natural Numbers")
    simple_test(number_names_str(hyphen=True),16,
                "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen")
    
    print("\nRoman Numerals")
    simple_test(roman_numerals_str(), 13,
                "I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII")
    
    print("\nRoman Numerals (numeric)")
    simple_test(roman_numerals(), 6,
                "(1,), (1, 1), (1, 1, 1), (1, 5), (5,), (5, 1)")
    