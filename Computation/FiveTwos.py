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


def five_twos_simple_comp():
    """Five Twos going only left to right, operations: +-*/^, can start with 22 by concatenation"""
    
    global N
    N = []
    global S
    S = []
    
    def five_twos_inner(val,sq,depth):
        
        if depth == 5:
            if int(val) == val and val >= 0:
                N.append(int(val))
                S.append(f"{sq} = {int(val)}")
            return 0
        
        funcs = [op.add, op.sub, op.mul, op.truediv, op.pow]
        
        if sq == "((((2":
            five_twos_inner(22,sq+"2",depth+1)
        
        for F,sym in zip(funcs,"+-*/^"):
            five_twos_inner(F(val,2),sq+f" {sym} 2)",depth+1)
    
    five_twos_inner(2,"((((2",1)
    
    return N,S


def five_twos_trans():
    """Five Twos with any grouping: +-*/"""
    
    global S
    S = []
    
    def five_twos_inner(st,depth):
        
        # Allow for concatenation of a 2 with another 2
        for pos in range(0,len(st)):
            if st[pos:pos+1] == "2":
                S.append(st[:pos] + "2"*(6-depth) + st[pos+1:])
    
        if depth == 5:
            S.append(st)
            return 0
        
        # Rewrite 2 as
        transforms = ["(2+2)","(2-2)","(2*2)","(2/2)","(2**2)"]
        
        for replacement in transforms:
            for pos in range(0,len(st)):
                if st[pos:pos+1] == "2":
                    five_twos_inner(st[:pos] + replacement + st[pos+1:],depth+1)
        
    five_twos_inner("2",1)
    
    return S


five_twos_simple()
print(sorted(list(set(N))))
print()

five_twos_simple_comp()
print(sorted(list(set(N))))
print()


five_twos_trans()
U = []
for st in S:
    try:
        if st.count("**") > 1:
            continue
        e = eval(st)
        if e == int(e) and e >= 0:
            if e in U:
                continue
            print(f"{st.replace('**','^')} = {int(e)}")
            U.append(int(e))
    except:
        pass