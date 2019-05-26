class Decimal:
    
    def __init__(self,digits,precision=20):
        
        ds = digits.count(".")
        if ds > 1:
            raise Exception("Not a valid decimal")
        if ds == 0:
            digits += "."
                    
        dgs = []
        dec = 0
        for ctr,i in enumerate(digits):
            if i.isdecimal():
                dgs.append(int(i))
            else:
                dec = ctr

        self.digits = dgs
        self.decpos = dec

#    def inv(self):
#
#
#    def __neg__(self):


    def __str__(self):
        w = [str(i) for i in self.digits[:self.decpos]]
        f = [str(i) for i in self.digits[self.decpos:]]
        return "".join(w) + "." + "".join(f)


    def __repr__(self):
        w = [str(i) for i in self.digits[:self.decpos]]
        f = [str(i) for i in self.digits[self.decpos:]]
        return "".join(w) + "." + "".join(f)


#    def __mul__(self,multiplier):
#
#
#    def __rmul__(self,multiplier):
#
#
#    def __truediv__(self,divisor):
#
#
#    def __add__(self,addend):
#
#
#    def __radd__(self,addend):
#
#
#    def __sub__(self,addend):
#
#
#    def __rsub__(self,addend):
#
#
#    def __eq__(self,other):
#
#
#    def __le__(self, other):
#
#        
#    def __lt__(self, other):
#
#
#    def __ge__(self, other):
#    
#    
#    def __gt__(self, other):
#
#    
#    def __pow__(self,power):
#
#
#    def __hash__(self):
#
#        
#    def whole_part(self):
#
#
#    def fractional_part(self):
#
#    
#    def mixed_form(self):

#a = Decimal("1001.20")
#print(a)