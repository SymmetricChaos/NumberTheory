from Numerals.BaseConvert import base_convert

def valid_digits(L,b):
    B = [i for i in range(b)]
    for i in L:
        if i not in B:
            return False
    return True

def baseN_sum(X,Y,base):
    X = X[:]
    Y = Y[:]
    while len(X) < len(Y):
        X.insert(0,0)
    while len(Y) < len(X):
        Y.insert(0,0)
        
    carry = 0
    out = []
    for a,b in zip(reversed(X),reversed(Y)):
        carry, digit = divmod(a+b+carry,base)
        out.append(digit)
    out.append(carry)
    
    out.reverse()
    
    while out[0] == 0:
        del out[0]
    
    return out
        


class BaseN:
    
    
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self,number,b):
        if type(number) == int:
            self.digits = base_convert(number,b)
            self.b = b
            assert valid_digits(self.digits,b)
            
        if type(number) == list:
            self.digits = number
            self.b = b
            assert valid_digits(self.digits,b)
    

    def __str__(self):
        if self.b <= 36:
            return "".join([self.alphabet[d] for d in self.digits])
        else:
            return " ".join(str(d) for d in self.digits)
    
    
    def __repr__(self):
        if self.b <= 36:
            return "".join([self.alphabet[d] for d in self.digits])
        else:
            return " ".join(str(d) for d in self.digits)


    def __int__(self):
        out = 0
        for pos,val in enumerate(self.digits[::-1]):
            out += val*self.b**pos
        return out
    
    def __add__(self,addend):
        assert self.b == addend.b
        d = baseN_sum(self.digits,addend.digits)
        return BaseN(d,self.b)