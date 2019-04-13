from EllipticCurveOOP import elliptic, elliptic_mult, elliptic_add

curve = elliptic(2,3,97)
P = (3,6)
Gs = []

print(curve.points)

for i in range(3):
    print(elliptic_mult(P,i,curve))
