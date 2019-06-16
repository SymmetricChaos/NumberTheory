def dec_to_bal_tern(n):
    assert type(n) == int
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
    digits.reverse()
    return digits


def bal_tern_to_dec(D):
    assert type(D) == list
    for i in D:
        if i not in [1,0,-1]:
            raise Exception("Not a balanced ternary string.")
    out = 0
    for pos,val in enumerate(D[::-1]):
        out += val*3**pos
    return out


str_to_int = {"+": 1, "0": 0, "-": -1}
int_to_str = {1: "+", 0: "0", -1: "-"}

class BalancedTernary:
            
    
    def __init__(self,n):
        if type(n) == int:
            self.digits = dec_to_bal_tern(n)
            self.n = n
        if type(n) == list:
            self.digits = n
            self.n = bal_tern_to_dec(n)
        if type(n) == str:
            self.digits = [str_to_int[s] for s in n]
            self.n = bal_tern_to_dec(self.digits)


    def __int__(self):
        return self.n


    def __str__(self):
        return "".join([int_to_str[s] for s in self.digits])


    def __repr__(self):
        return "".join([int_to_str[s] for s in self.digits])
    
    
    def __add__(self,addend):
        return BalancedTernary(self.n+addend.n)
        
        
    def __radd__(self,addend):
        return BalancedTernary(self.n+addend.n)


    def __mul__(self,multiplicand):
        return BalancedTernary(self.n*multiplicand.n)


    def __rmul__(self,multiplicand):
        return BalancedTernary(self.n*multiplicand.n)