from Sequences.Simple import odds


def rule_30(V=(1,)):
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
    
    while True:
        yield V
        
        V = (0,0) + V + (0,0)
        
        new = []
        for i in range(len(V)-2):
            new.append(D[V[i:i+3]])
        
        V = tuple(new)


def rule_30_black(V=(1,)):
    """
    Black Cells in Each Row of the Rule 30 Triangle
    """
    
    for R in rule_30(V):
        yield sum(R)


def rule_30_white(V=(1,)):
    """
    White Cells in Each Rows of the Rule 30 Triangle
    """
    
    for o,R in zip(odds(),rule_30(V)):
        yield o-sum(R)


def rule_90(V=(1,)):
    """
    Irregular Triangle of Rule 90 by Rows\n
    """
    
    D = {(1,1,1): 0,
         (1,1,0): 1,
         (1,0,1): 0,
         (1,0,0): 1,
         (0,1,1): 1,
         (0,1,0): 0,
         (0,0,1): 1,
         (0,0,0): 0,}
    
    while True:
        yield V
        
        V = (0,0) + V + (0,0)
        
        new = []
        for i in range(len(V)-2):
            new.append(D[V[i:i+3]])
        
        V = tuple(new)


def rule_90_black(V=(1,)):
    """
    Black Cells in Each Row of the Rule 90 Triangle
    """
    
    for R in rule_90(V):
        yield sum(R)


def rule_90_white(V=(1,)):
    """
    White Cells in Each Rows of the Rule 90 Triangle
    """
    
    for o,R in zip(odds(),rule_90(V)):
        yield o-sum(R)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nRule 30")
    simple_test(rule_30(),5,
                "(1,), (1, 1, 1), (1, 1, 0, 0, 1), (1, 1, 0, 1, 1, 1, 1), (1, 1, 0, 0, 1, 0, 0, 0, 1)")
    
    print("\nRule 30 Black")
    simple_test(rule_30_black(),16,
                "1, 3, 3, 6, 4, 9, 5, 12, 7, 12, 11, 14, 12, 19, 13, 22")
    
    print("\nRule 30 White")
    simple_test(rule_30_white(),17,
                "0, 0, 2, 1, 5, 2, 8, 3, 10, 7, 10, 9, 13, 8, 16, 9, 18")
    
    print("\nRule 90")
    simple_test(rule_90(),5,
                "(1,), (1, 0, 1), (1, 0, 0, 0, 1), (1, 0, 1, 0, 1, 0, 1), (1, 0, 0, 0, 0, 0, 0, 0, 1)")
    
    print("\nRule 90 Black")
    simple_test(rule_90_black(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nRule 90 White")
    simple_test(rule_90_white(),16,
                "0, 1, 3, 3, 7, 7, 9, 7, 15, 15, 17, 15, 21, 19, 21, 15")
    