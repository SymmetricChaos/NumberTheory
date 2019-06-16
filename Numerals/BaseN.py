from Numerals.BaseConvert import base_convert

def valid_digits(L,b):
    B = [i for i in range(b)]
    for i in L:
        if i not in B:
            return False
    return True

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class BaseN:
    
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
            return "".join([alphabet[d] for d in self.digits])
        else:
            return " ".join(str(d) for d in self.digits)
    
    
    def __repr__(self):
        if self.b <= 36:
            return "".join([alphabet[d] for d in self.digits])
        else:
            return " ".join(str(d) for d in self.digits)


    def __int__(self):
        out = 0
        for pos,val in enumerate(self.digits[::-1]):
            out += val*self.b**pos
        return out