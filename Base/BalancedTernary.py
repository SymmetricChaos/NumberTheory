def balanced_ternary(n):
    digits = []
    while n != 0:
        if n % 3 == 0:
            digits.append(0)
            n = n // 3
        if n % 3 == 1:
            digits.append(1)
            n = n // 3
        if n % 3 == 2:
            digits.append(-1)
            n = (n+1) // 3
    return digits
    

str_to_int = {"+": 1, "0": 0, "-": -1}
int_to_str = {1: "+", 0: "0", -1: "-"}

class BalancedTernary:
            
    
    def __init__(self,n):
        if type(n) == int:
            self.digits = balanced_ternary(n)
        if type(n) == str:
            self.digits = [int_to_str[s] for s in n]
        self.digits.reverse()


    def __int__(self):
        out = 0
        for pos,val in enumerate(self.digits[::-1]):
            out += val*3**pos
        return out


    def __str__(self):
        return "".join([int_to_str[s] for s in self.digits])


    def __repr__(self):
        return "".join([int_to_str[s] for s in self.digits])


for i in range(10000):
    t = BalancedTernary(i)
    print(i,t)
    if int(t) != i:
        break