def poly_print_simple(poly,pretty=False):
    """Show the polynomial in descending form as it would be written"""
        
    # Get the degree of the polynomial in case it is in non-normal form
    d = poly.degree()
    
    if d == -1:
        return f"0"

    out = ""
    
    # Step through the ascending list of coefficients backward
    # We do this because polynomials are usually written in descending order
    for pwr in range(d,-1,-1):
        
        # Skip the zero coefficients entirely
        if poly[pwr] == 0:
            continue
        
        coe = poly[pwr]
        val = abs(coe)
        sgn = "-" if coe//val == -1 else "+"
                
        # When the coefficient is 1 or -1 don't print it unless it is the
        # coefficient for x^0
        if val == 1 and pwr != 0:
            val = ""
  
        # If it is the first term include the sign of the coefficient
        if pwr == d:
            if sgn == "+":
                sgn = ""
            
            # Handle powers of 1 or 0 that appear as the first term
            if pwr == 1:
                s = f"{sgn}{val}x"
            elif pwr == 0:
                s = f"{sgn}{val}"
            else:
                if pretty == False:
                    s = f"{sgn}{val}x^{pwr}"
                else:
                    s = f"{sgn}{val}x$^{{{pwr}}}$"
                    
        
        # If the power is 1 just show x rather than x^1
        elif pwr == 1:
            s = f" {sgn} {val}x"
        
        # If the power is 0 only show the sign and value
        elif pwr == 0:
            s = f" {sgn} {val}"
        
        # Otherwise show everything
        else:
            if pretty == False:
                s = f" {sgn} {val}x^{pwr}"
            else:
                s = f" {sgn} {val}x$^{{{pwr}}}$"
        out += s
    return out