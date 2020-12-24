def fractal_tree_str():
    """
    IFS that produces a string that can be used to draw generations of a fractal tree
    """
    
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


def koch_curve_str():
    """
    IFS that produces a string that can be used to draw generations of the Koch Curve
    """
    
    D = {"F": "F+F-F-F+F",
         "+": "+",
         "-": "-"}
    
    S = "F"
    
    while True:
        yield S
        
        t = ""
        
        for s in S:
            t += D[s]
        
        S = t





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("Fractal Tree")
    simple_test(fractal_tree_str(),4,
                "0, 1[0]0, 11[1[0]0]1[0]0, 1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0")
    
    print("\nKoch Curve")
    simple_test(koch_curve_str(),3,
                "F, F+F-F-F+F, F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F")