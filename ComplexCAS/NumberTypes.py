class Symbol:
    
    def __init__(self,S):
        if type(S) != str:
            raise TypeError("Symbols must be strings")
        if S not in "abcdefghijklmnopqrstuvwxyz":
            raise ValueError("Symbols must be lowercase letters")

        self.S = S
        
    def __str__(self):
        return self.S





class Power:
    
    def __init__(self,b,p):
        self.b = b
        self.p = p
    
    def simplify(self):
        pass

    def __str__(self):
        return f"{self.b}^{self.p}"



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
            out += f"+ ({i})"
        return out
        
        

class Ratio:
    
    def __init__(self,N,D):
        self.N = N
        self.D = D