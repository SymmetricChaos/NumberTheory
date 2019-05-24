class Decimal:
    
    def __init__(self,dec):
        assert type(dec) == str
        for i in dec:
            if i not in ".0123456789":
                raise Exception("Not a valid decimal")
        if dec.count() > 1:
            raise Exception("Not a valid decimal")
            
        while dec[0] == "0":
            dec = dec[1:]
        while dec[-1] == "0":
            dec = dec[:-1]
        
        self.digits = dec


#    def inv(self):
#
#
#    def __neg__(self):


    def __str__(self):
        return self.digits


    def __repr__(self):
        return self.digits


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


    def __eq__(self,other):
        return self.digits == other.digits
    

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

