from MathUtils import _bits_to_int

# Obviously these are all VERY inefficient

def LCG(x,a,c,m):
    """Linear Congruential Generator"""
    
    while True:
        yield x
        x = ((a*x)+c)%m


def LFG(a,b,m,func):
    """Lagged Fibonacci Generator"""
    
    while True:
        yield a
        a,b = b,func(a,b)%m


def FLFSR_bits(vector,taps):
    """Fibonacci Linear Feedback Shift Register: Returns the lowest order bit at each step"""
    
    if type(vector) != list:
        raise Exception("The vector must be a list")
    if type(taps) != list:
        raise Exception("The taps must be a list")
    
    for v in vector:
        if v not in (0,1):
            raise Exception("Vector must consist only of 1s and 0s")
    for t in taps:
        if t >= len(vector):
            raise Exception("Taps must be valid positions in the vector")
    
    while True:
        yield vector[0]
        vector = vector[1:] + [sum([vector[i] for i in taps])%2]


def FLFSR(vector,taps):
    """Fibonacci Linear Feedback Shift Register: Returns the state at each step"""
    
    if type(vector) != list:
        raise Exception("The vector must be a list")
    if type(taps) != list:
        raise Exception("The taps must be a list")
    
    for v in vector:
        if v not in (0,1):
            raise Exception("Vector must consist only of 1s and 0s")
    for t in taps:
        if t >= len(vector):
            raise Exception("Taps must be valid positions in the vector")
    
    while True:
        yield _bits_to_int(vector)
        vector = vector[1:] + [sum([vector[i] for i in taps])%2]





if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Linear Congruential Generator")
    simple_test(LCG(9,5,17,97),10,
                "9, 62, 36, 3, 32, 80, 29, 65, 51, 78")
    
    print("\nLagged Fibonacci Generator")
    simple_test(LFG(9,27,97,lambda x,y:x*y),10,
                "9, 27, 49, 62, 31, 79, 24, 53, 11, 1")
    
    print("\nFibonacci Linear Feedback Shift Register")
    simple_test(FLFSR_bits([1,0,0,1],[0,3]),10,
                "1, 0, 0, 1, 0, 0, 0, 1, 1, 1")
    
    print("\nFibonacci Linear Feedback Shift Register")
    simple_test(FLFSR([1,0,0,1,0,1,1,0],[0,3,6,7]),10,
                "105, 180, 218, 237, 118, 187, 221, 110, 55, 155")
    