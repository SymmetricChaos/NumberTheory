Roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

# Ones, tens, and hundred digits
R1   = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
R10  = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
R100 = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]

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


def int_to_roman(n):
    
    d = [int(i) for i in str(n%1000)]
    
    L = ["M"]*(n//1000)
    
    L.append( R100[d[0]] )
    L.append( R10[d[1]] )
    L.append( R1[d[2]] )
    
    return "".join(L)
    

print(roman_to_int("MCMLIV"))

print(int_to_roman(1954))