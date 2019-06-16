from Polynomials import Polynomial
from Combinatorics.Distributions import BinomialDist

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
print("\nWhen events are mutually exclusive the probability of both happening comes from adding them together. Since each possible permutation is mutually exclusive we can in fact add them together. That justifies summing terms with the same order.")
b = BinomialDist(3,.4)