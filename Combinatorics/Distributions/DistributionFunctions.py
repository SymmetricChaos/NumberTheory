from math import sqrt

def std_dev(distribution):
    return sqrt(distribution.var)

def is_prob(p):
    assert p > 0, "probability must be greater than zero"
    assert p < 1, "probability must be less than one"
    return True