from Numerals import BijectiveBase
from random import randint


A = BijectiveBase(4354,9)
B = BijectiveBase(1726,9)
print(A," + ",B," = ",A+B)
print("We can change the symbols used to represent the digits.")
BijectiveBase.ALPHA = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
print(A," + ",B," = ",A+B)