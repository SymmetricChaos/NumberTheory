class Symbol:
    
    def __init__(self,S,sign=1):
        if type(S) != str:
            raise TypeError("Symbols must be strings")
        if S not in "abcdefghijklmnopqrstuvwxyz":
            raise ValueError("Symbols must be lowercase letters")

        self.S = S
        self.sign = sign


    def __str__(self):
        if self.sign == 1:
            return self.S
        else:
            return f"-{self.S}"


    def __eq__(self,other):
        if type(other) == Symbol:
            if other.S == self.S:
                return True
        return False


    def __neg__(self):
        return Symbol(self.S,self.sign*-1)


    def __add__(self,other):
        if self == other:
            return Product([2,self])
        else:
            return Sum([self,other])










###############
## Combiners ##
###############
class Product:
    
    def __init__(self,L):
        if type(L) != list:
            raise TypeError("Products must be lists")
        
        self.L = L
        
    
    def simplify(self):
        pass


    def __str__(self):
        out = ""
        for i in self.L:
            out += f"{i}"
        return out



class Sum:
    
    def __init__(self,L):
        if type(L) != list:
            raise TypeError("Sums must be lists")
        
        self.L = L
        
    def simplify(self):
        pass
    
    def __str__(self):
        out = ""
        for i in self.L:
            out += f" + {i}"
        return out



        

#class Ratio:
#    
#    def __init__(self,N,D):
#        self.N = N
#        self.D = D
#        
#    def simplify(self):
#        pass
#    
#    def __str__(self):
#        return f"({self.N})/({self.D})"
#
#
#
#
#
#class Power:
#    
#    def __init__(self,b,p):
#        self.b = b
#        self.p = p
#    
#    def simplify(self):
#        pass
#
#    def __str__(self):
#        return f"{self.b}^{self.p}"