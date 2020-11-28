from Sequences.Simple import odds


def rule_30():
    """
    Irregular Triangle of Rule 30 by Rows\n
    OEIS A070952
    """
    
    D = {(1,1,1): 0,
         (1,1,0): 0,
         (1,0,1): 0,
         (1,0,0): 1,
         (0,1,1): 1,
         (0,1,0): 1,
         (0,0,1): 1,
         (0,0,0): 0,}
    
    S = (1,)
    
    while True:
        yield S
        
        S = (0,0) + S + (0,0)
        
        new = []
        for i in range(len(S)-2):
            new.append(D[S[i:i+3]])
        
        S = tuple(new)


def rule_30_black():
    """
    Black Cells in Each Row of the Rule 30 Triangle
    """
    
    for R in rule_30():
        yield sum(R)


def rule_30_white():
    """
    White Cells in Each Rows of the Rule 30 Triangle
    """
    
    for o,R in zip(odds(),rule_30()):
        yield o-sum(R)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    
    print("Rule 30")
    simple_test(rule_30(),5,
                "(1,), (1, 1, 1), (1, 1, 0, 0, 1), (1, 1, 0, 1, 1, 1, 1), (1, 1, 0, 0, 1, 0, 0, 0, 1)")
    
    print("\nRule 30 Black")
    simple_test(rule_30_black(),16,
                "1, 3, 3, 6, 4, 9, 5, 12, 7, 12, 11, 14, 12, 19, 13, 22")
    
    print("\nRule 30 White")
    simple_test(rule_30_white(),17,
                "0, 0, 2, 1, 5, 2, 8, 3, 10, 7, 10, 9, 13, 8, 16, 9, 18")
    