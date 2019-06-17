from Polynomials import Polynomial
from Rationals import Rational

print("Say we have a biased coin. It has P(Heads) = .6 and P(Tails) = .4 which we could represent as a Bernoulli distribution. However another option is to encode it as a polynomial generating function. That would be:")

Bern = Polynomial([.4,.6])
print(Bern)

print("\nTHis is useful because the coefficients of polynomials distribute over each other when multiplying. That is exactly what happens when we try to calculate the probabilities associated with flipping the coin multiple times.")

print("")

for i in range(2,6):
    Bin = Bern**i
    print(round(Bin,2))
    
print("""
Let's see why with two coin flips (removing decimals for ease of reading)
(6x + 4) * (6x + 4)
6x*6x + 6x*4 + 6x*4 + 4*4
36x^2 + 48x + 16
""")

print("The probability of independent events both happening comes from multiplying together the probability of each. This is exactly what happens when we distribute the coefficients for polynomial multiplication, every pair gets multiplied together.")
print("\nWhen events are mutually exclusive the probability of both happening comes from adding them together. Since each possible permutation is mutually exclusive we can in fact add them together. That justifies summing terms we consider equivalent.")

print("\n\nEven better this means that we can easily generalize to more interesting distributions like the multinomial.")

print("\nSay we have a die with the sides {1,2,3,4,5,6} we can represent this as a polynomial like this.")

c = Rational(1,6)
dice = Polynomial([0,c,c,c,c,c,c])
print(dice)

print("\nNotice that we have no zeroth order coefficient because there is no side with a value of 0.")
print("\nFor the same reasons that we can represent multiple coins by multiplying together their generating functions together we can multiply the generating functions for dice together.")
print("\nSo if we multiply three dice together:\n")

A = dice**3
pA = Polynomial([round(float(i),3) for i in A.coef])

print(pA)

print("\nNotice that there are no terms of order 0, 1, or 2 since those outcomes are not possible. You cannot roll three ordinary dice and get a sum of 2.")
