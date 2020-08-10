def thue_morse():
    """Thue-Morse Sequence"""
    
    S = [0]
    
    yield 0
    
    while True:
        new = []
        
        for s in S:
            yield (s+1)%2
            new.append((s+1)%2)
            
        S += new