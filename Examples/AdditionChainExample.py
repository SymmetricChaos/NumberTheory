from Computation import addition_chain
from GeneralUtils import equal_spacing

for i in range(1,50):
    equal_spacing(addition_chain(i),3,'center')