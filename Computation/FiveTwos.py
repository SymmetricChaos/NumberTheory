import operator as op


def five_twos_simple():
    """Five Twos going only left to right, operations: +-*/^"""
    
    global N
    N = []
    global S
    S = []
    
    def five_twos_inner(val,sq,depth):
        
        if depth == 5:
            if int(val) == val and val >= 0:
                N.append(int(val))
                S.append(sq)
            return 0
        
        funcs = [op.add, op.sub, op.mul, op.truediv, op.pow]
        
        for F,sym in zip(funcs,"+-*/^"):
            five_twos_inner(F(val,2),sq+f" {sym} 2)",depth+1)
    
    five_twos_inner(2,"((((2",1)
    
    return N,S


N,S = five_twos_simple()

print(sorted(list(set(N))))