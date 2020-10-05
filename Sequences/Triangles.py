from Sequences.Manipulations import make_triangle, sequence_apply, irregular_array
from Sequences.Combinatorics import pascal, eulerian
from Sequences.Weird import gcd_numbers, gcd_steps, sierpinski
from Sequences.Divisibility import coprime_characteristic
from Sequences.MathUtils import triangle_pairs, antidiagonal_pairs
from Sequences.Fractional import _pretty_fracs, fibonacci_generations
from Sequences.Simple import powers


def quick_triangle(sequence,n,space=0,delim=" "):
    
    T = make_triangle(sequence)
    
    for i in range(n):
        l = [f"{str(x):<{space}}" for x in next(T)]
        s = str(delim).join(l)
        print(s)


def quick_array(sequence,row_lengths,n,space=0,delim=" "):
    
    T = irregular_array(sequence,row_lengths)
    
    for i in range(n):
        l = [f"{str(x):<{space}}" for x in next(T)]
        s = str(delim).join(l)
        print(s)





if __name__ == '__main__':
    
    print("Pascal's Triangle")
    quick_triangle(pascal(),10,2)
    
    print("\nSierpinski's Triangle")
    quick_triangle(sequence_apply(sierpinski(),lambda x: "#" if x == 1 else " "),16,delim="")
    
    print("\nEuler's Triangle")
    quick_triangle(eulerian(),6,2)
    
    print("\nGCD Triangle")
    quick_triangle(gcd_numbers(),10,1)
    
    print("\nGCD Step Triangle")
    quick_triangle(gcd_steps(),10,2)
    
    print("\nCoprime Triangle")
    quick_triangle(coprime_characteristic(),10,1)
    
    print("\nIdicies of a Regular Triangular Array")
    quick_triangle(triangle_pairs(),7,1)
    
    print("\nIndicies of the Antidiagonals of a Square Array")
    quick_triangle(antidiagonal_pairs(),7,1)
    
    print("\nEach Generations of Rationals Using the Fibonacci Method")
    quick_array(_pretty_fracs(fibonacci_generations()),powers(2),4,1)