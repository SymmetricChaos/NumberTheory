def thue_morse(s=0):
    """
    Thue-Morse Sequence
    OEIS A010060, A010059
    """
    
    if s not in (0,1):
        raise ValueError("The Thue-Morse Sequence must start with either 0 or 1")
    
    S = [s]
    
    yield s
    
    while True:
        new = []
        
        for s in S:
            yield (s+1)%2
            new.append((s+1)%2)
            
        S += new


if __name__ == '__main__':
    from Sequences.SequenceManipulation import simple_test
    
    print("Thue-Morse Sequence")
    simple_test(thue_morse(0),16,
                "0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0")
    
    print("\nComplement of the Thue-Morse Sequence")
    simple_test(thue_morse(1),16,
                "1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1")