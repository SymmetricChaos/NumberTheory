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

b = BinomialDist(3,.4)