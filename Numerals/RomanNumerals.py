Roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}


def roman_to_int(n):
    out = 0
    L = []
    
    # Convert the Roman numerals to integer values
    for r in n:
        L.append(Roman[r])
    
    # Step through the numerals adding or subtracting as needed
    for i in range(len(L)-1):
        a, b = L[i],L[i+1]
        if a >= b:
            out += a
        else:
            out -= a
    
    # The final Roman numeral is always added
    out += L[-1]
            
    return out


#def int_to_roman(n):
    

print(roman_to_int("MCMLIV"))