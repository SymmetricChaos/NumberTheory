from EllipticCurveOOP import elliptic, elliptic_mult

curve = elliptic(2,3,97)
P = (3,6)
Q = (80,10)

for i in range(10):
    print(elliptic_mult(Q,i,curve))