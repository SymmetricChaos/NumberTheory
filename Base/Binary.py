from Base.BaseConvert import base_convert

def valid_binary(L):
    for i in L:
        if i != 0 or i != 1:
            return False
    return True

class Binary:
    
    def __init__(self,number):
        if type(number) == int:
            self.digits = base_convert(number,2)
            
        if type(number) == list:
            self.digits = number
            #assert valid_binary(self.digits)
            
        if type(number) == str:
            self.digits = [int(i) for i in number]
            #assert valid_binary(self.digits)
    
    def __str__(self):
        return "".join([str(d) for d in self.digits])
    
    def __repr__(self):
        return "".join([str(d) for d in self.digits])

    def __int__(self):
        out = 0
        for pos,val in enumerate(self.digits[::-1]):
            out += val*2**pos
        return out