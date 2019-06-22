from Numerals import int_to_roman
from random import randint

for i in range(15):
    n = randint(1,3000)
    print(f"{n:<4} = {int_to_roman(n)}")