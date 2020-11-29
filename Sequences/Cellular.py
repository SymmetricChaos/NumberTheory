from Sequences.Simple import odds

R30 = {(1,1,1): 0,
       (1,1,0): 0,
       (1,0,1): 0,
       (1,0,0): 1,
       (0,1,1): 1,
       (0,1,0): 1,
       (0,0,1): 1,
       (0,0,0): 0}

R30_str = {"###": " ",
           "## ": " ",
           "# #": " ",
           "#  ": "#",
           " ##": "#",
           " # ": "#",
           "  #": "#",
           "   ": " "}

R90 = {(1,1,1): 0,
       (1,1,0): 1,
       (1,0,1): 0,
       (1,0,0): 1,
       (0,1,1): 1,
       (0,1,0): 0,
       (0,0,1): 1,
       (0,0,0): 0}

R90_str = {"###": " ",
           "## ": "#",
           "# #": " ",
           "#  ": "#",
           " ##": "#",
           " # ": " ",
           "  #": "#",
           "   ": " "}

R110 = {(1,1,1): 0,
        (1,1,0): 1,
        (1,0,1): 1,
        (1,0,0): 0,
        (0,1,1): 1,
        (0,1,0): 1,
        (0,0,1): 1,
        (0,0,0): 0}

R110_str = {"###": " ",
            "## ": "#",
            "# #": "#",
            "#  ": " ",
            " ##": "#",
            " # ": "#",
            "  #": "#",
            "   ": " "}


def make_wolfram_code(rule_code,rule_code_str):
    
    def RULE(V=(1,)):
    
        while True:
            yield V
            
            V = (0,0) + V + (0,0)
            
            new = []
            for i in range(len(V)-2):
                new.append(rule_code[V[i:i+3]])
            
            V = tuple(new)
    
    
    def RULE_str(V="#"):
        
        while True:
            yield V
            
            V = "  " + V + "  "
            
            new = ""
            for i in range(len(V)-2):
                new += rule_code_str[V[i:i+3]]
            
            V = new
    
    
    def RULE_black(V=(1,)):
        
        for R in RULE(V):
            yield sum(R)
    
    
    def RULE_white(V=(1,)):
        
        for o,R in zip(odds(),RULE(V)):
            yield o-sum(R)
    
    return RULE, RULE_str, RULE_black, RULE_white


rule_30, rule_30_str, rule_30_black, rule_30_white = make_wolfram_code(R30,R30_str)
rule_90, rule_90_str, rule_90_black, rule_90_white = make_wolfram_code(R90,R90_str)
rule_110, rule_110_str, rule_110_black, rule_110_white = make_wolfram_code(R110,R110_str)





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nRule 30")
    simple_test(rule_30_str(),6,
                "#, ###, ##  #, ## ####, ##  #   #, ## #### ###")
    
    print("\nRule 30 Black")
    simple_test(rule_30_black(),16,
                "1, 3, 3, 6, 4, 9, 5, 12, 7, 12, 11, 14, 12, 19, 13, 22")
    
    print("\nRule 30 White")
    simple_test(rule_30_white(),17,
                "0, 0, 2, 1, 5, 2, 8, 3, 10, 7, 10, 9, 13, 8, 16, 9, 18")
    
    print("\nRule 90")
    simple_test(rule_90_str(),6,
                "#, # #, #   #, # # # #, #       #, # #     # #")
    
    print("\nRule 90 Black")
    simple_test(rule_90_black(),18,
                "1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4")
    
    print("\nRule 90 White")
    simple_test(rule_90_white(),16,
                "0, 1, 3, 3, 7, 7, 9, 7, 15, 15, 17, 15, 21, 19, 21, 15")
    
    print("\nRule 110")
    simple_test(rule_110_str(),6,
                "#, ## , ###  , ## #   , #####    , ##   #     ")
    
    print("\nRule 110 Black")
    simple_test(rule_110_black(),17,
                "1, 2, 3, 3, 5, 3, 5, 6, 8, 5, 6, 8, 8, 8, 11, 11, 13")
    
    print("\nRule 110 White")
    simple_test(rule_110_white(),16,
                "0, 1, 2, 4, 4, 8, 8, 9, 9, 14, 15, 15, 17, 19, 18, 20")
    