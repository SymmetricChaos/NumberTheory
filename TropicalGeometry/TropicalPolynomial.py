from TropicalSemiring import Tropical

class TropicalPoly:
    
    def __init__(self,coef):
        assert type(coef) == list
        self.coef = [Tropical(c) for c in coef]
        
    def __getitem__(self,n):
        return self.coef[n]
    
    def degree(self):
        return len(self.coef)-1
    
    def __len__(self):
        return len(self.coef)
    
    def __eq__(self,poly):
        if len(self) == len(poly):
            if all([x == y for x,y in zip(self.coef,poly.coef)]):
                return True
        return False
    
    def __str__(self):
        
        d = self.degree()
    
        if d == -1:
            return "0"

        out = ""
    
        # Step through the ascending list of coefficients backward
        # We do this because polynomials are usually written in descending order
        for pwr in range(d,-1,-1):
            
            # Skip the zero coefficients entirely
            if self[pwr] == 0:
                continue
            
            coe = self[pwr]
            val = abs(coe)
            sgn = "-" if coe < 0 else "+"
                    
            # When the coefficient is 1 or -1 don't print it unless it is the
            # coefficient for x^0
            if val == 1 and pwr != 0:
                val = ""
      
            # If it is the first term include the sign of the coefficient
            if pwr == d:
                if sgn == "+":
                    sgn = ""
                
                # Handle powers of 1 and zero that appear as the first term
                if pwr == 1:
                    s = "{}{}x".format(sgn,val)
                elif pwr == 0:
                    s = "{}{}".format(sgn,val)
                else:
                    s = "{}{}x^{}".format(sgn,val,pwr)
            
            # If power is 1 just show x rather than x^1
            elif pwr == 1:
                s = " {} {}x".format(sgn,val)
            
            # If the power is 0 only show the sign and value
            elif pwr == 0:
                s = " {} {}".format(sgn,val)
            
            # Otherwise show the sign, coefficient, and power
            else:
                s = " {} {}x^{}".format(sgn,val,pwr)
            
            out += s
        
        return out
    
    
    def evaluate(self,X):
        """Evaluate the polynomial at a given point or points"""
        if type(X) != list:
            X = [X]
        out = [float('inf')]*len(X)
        for pwr,coef in enumerate(self.coef):
            for pos,x in enumerate(X):
                out[pos] = out[pos] + coef*(Tropical(x)**pwr)
        
        if len(out) == 1:
            return out[0]
        return out