from Sequences.SequenceManipulation import make_triangle
from Sequences.Combinatorics import pascal, eulerian
from Sequences.Weird import gcd_numbers, gcd_steps
from Sequences.Primes import coprime_characteristic
from Sequences.MathUtils import triangle_pairs, antidiagonal_pairs

def quick_triangle(sequence,n,space=0,delim=" "):
    
    T = make_triangle(sequence)
    
    for i in range(n):
        l = [f"{str(x):<{space}}" for x in next(T)]
        s = str(delim).join(l)
        print(s)





if __name__ == '__main__':
    
    print("Pascal's Triangle")
    quick_triangle(pascal(),10,2)
    
    print("\nEuler's Triangle")
    quick_triangle(eulerian(),6,2)
    
    print("\nGCD Triangle")
    quick_triangle(gcd_numbers(),10,1)
    
    print("\nGCD Step Triangle")
    quick_triangle(gcd_steps(),10,1)
    
    print("\nCoprime Triangle")
    quick_triangle(coprime_characteristic(),10,1)
    
    print("\nIdicies")
    quick_triangle(triangle_pairs(),7,1)
    
    print("\nAntidiagonals of a Square Array")
    quick_triangle(antidiagonal_pairs(),7,1)