def poly_print(poly_mul):
    """Show the polynomial in descending form as it would be written"""
#    # Get the degree of the polynomial in case it is in non-normal form
#    d = poly_degree(P)
#    
#    if d == -1:
#        if mod == 0:
#            return f"0"
#        else:
#            return f"0 (mod {mod})"
#
#    
#    out = ""
    
    for term in poly_mul.T:
        sgn = "-" if term.C < 0 else "+"
        print(sgn,abs(term.C))
#    
#    # Step through the ascending list of coefficients backward
#    # We do this because polynomials are usually written in descending order
#    for pwr in range(d,-1,-1):
#        
#        # Skip the zero coefficients entirely
#        if P[pwr] == 0:
#            continue
#        
#        coe = P[pwr]
#        val = abs(coe)
#        sgn = "-" if coe//val == -1 else "+"
#                
#        # When the coefficient is 1 or -1 don't print it unless it is the
#        # coefficient for x^0
#        if val == 1 and pwr != 0:
#            val = ""
#  
#        # If it is the first term include the sign of the coefficient
#        if pwr == d:
#            if sgn == "+":
#                sgn = ""
#            
#            # Handle powers of 1 and zero that appear as the first term
#            if pwr == 1:
#                s = "{}{}x".format(sgn,val)
#            elif pwr == 0:
#                s = "{}{}".format(sgn,val)
#            else:
#                s = "{}{}x^{}".format(sgn,val,pwr)
#        
#        # If power is 1 just show x rather than x^1
#        elif pwr == 1:
#            s = " {} {}x".format(sgn,val)
#        
#        # If the power is 0 only show the sign and value
#        elif pwr == 0:
#            s = " {} {}".format(sgn,val)
#        
#        # Otherwise show the sign, coefficient, and power
#        else:
#            s = " {} {}x^{}".format(sgn,val,pwr)
#        
#        out += s
#    
#    if mod == 0:
#        return out
#    else:
#        out += " (mod {})".format(mod)
#        return out