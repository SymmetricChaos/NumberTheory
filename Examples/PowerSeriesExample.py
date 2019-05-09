from PowerSeries import geometric_series_convergents, power_series_convergents
from Sequences import factorials, partial

for x in [-.5,.13,.2]:
    print("Convergents of Geometric Series x = {}".format(x))
    for i in geometric_series_convergents(x,5):
        print("{:.5f}".format(i))
    print()

print("Convergents of the exponential function at x = 2")
inv_fact = [1] + [1/f for f in partial(factorials,11)]
for ctr,i in enumerate(power_series_convergents(2,inv_fact)):
    print("{:.5f}".format(i))
    if ctr > 10:
        break