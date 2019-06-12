from Combinatorics import narayana_number
from GeneralUtils import equal_spacing

for n in range(1,7):
    L = []
    for m in range(1,n+1):
        L.append(narayana_number(m,n))
    equal_spacing(L,4,'left')