from Sequences.Manipulations import make_triangle, irregular_array
from Sequences.Combinatorics import eulerian, sierpinski_triangle, pascal_triangle
from Sequences.Weird import gcd_numbers, gcd_steps
from Sequences.Divisibility import coprime_characteristic
from Sequences.MathUtils import triangle_pairs, antidiagonal_pairs
from Sequences.Fractional import _pretty_fracs, fibonacci_generations
from Sequences.Simple import powers


def pretty_array(A,n,space=0,delim=" "):
    for i in range(n):
        l = [f"{str(x):<{space}}" for x in next(A)]
        s = str(delim).join(l)
        print(s)


def quick_triangle(sequence,n,space=0,delim=" "):
    T = make_triangle(sequence)
    pretty_array(T,n=n,space=space,delim=delim)


def quick_array(sequence,row_lengths,n,space=0,delim=" "):
    A = irregular_array(sequence,row_lengths)
    pretty_array(A,n=n,space=space,delim=delim)





# if __name__ == '__main__':
    
#     print("\nPascal's Triangle")
#     pretty_array(pascal_triangle(),10,3)
    
#     print("\nSierpinski's Triangle")
#     pretty_array(sierpinski_triangle(),10)
    
#     print("\nEuler's Triangle")
#     quick_triangle(eulerian(),6,3)
    
#     print("\nGCD Triangle")
#     quick_triangle(gcd_numbers(),10,1)
    
#     print("\nGCD Step Triangle")
#     quick_triangle(gcd_steps(),10,2)
    
#     print("\nCoprime Triangle")
#     quick_triangle(coprime_characteristic(),10,1)
    
#     print("\nIdicies of a Regular Triangular Array")
#     quick_triangle(triangle_pairs(),7,1)
    
#     print("\nIndicies of the Antidiagonals of a Square Array")
#     quick_triangle(antidiagonal_pairs(),7,1)
    
#     print("\nEach Generations of Rationals Using the Fibonacci Method")
#     quick_array(_pretty_fracs(fibonacci_generations()),powers(2),4,1)