def fractal_tree_str():
    """"""
    
    D = {"1": "11",
         "0": "1[0]0",
         "[": "[",
         "]": "]"}
    
    S = "0"
    
    while True:
        yield S
        
        t = ""
        
        for s in S:
            t += D[s]
        
        S = t



if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Fractal Tree")
    simple_test(fractal_tree_str(),3,
                "0, 1[0]0, 11[1[0]0]1[0]0")
    