from math import isqrt

def continued_fraction(n,d):
    """
    Simple continued fraction representation sof n/d
    """
    
    while d != 0:
        i = n//d
        yield i
        
        n,d = d,n-(d*i)


# This can be sped up in the extreme case by using cycle detection
def sqrt_continued_fraction(n):
    
    a = a0 = isqrt(n)
    m,d = 0,1
    
    while True:
        yield a
        
        m = d*a-m
        d = (n-(m*m))//d
        a = (a0+m)//d



# def pi_continued_fraction():






if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Continued Fraction for 649/200")
    simple_test(continued_fraction(649,200),18,
                "3, 4, 12, 4")
    
    print("Continued Fraction for the √144")
    simple_test(sqrt_continued_fraction(114),16,
                "10, 1, 2, 10, 2, 1, 20, 1, 2, 10, 2, 1, 20, 1, 2, 10")
    