from Computation import binary_partition, exp_by_squaring

print("The naieve method for calculating exponents is to multiply a number by itself n times. This requires n-1 multiplications. However there are much more efficient ways to calculate positive integer exponents.")
print("In general the most efficient method is difficult to find. However it is easy to find very fast methods. In particular repeated squaring is quite efficient compare to the naieve method.")

b = 2
e = 471
print(f"For example we can calculate {b}^{e} by breaking {e} into the sum of {[2**i for i in binary_partition(e)]}")


def exp_by_squaring_example(b,n):
    p = binary_partition(n)
    #Multiplications needed
    print(len(p)+max(p)-1)
    t = b
    L = [f"{b}^1"]
    for i in range(p[-1]):
        t = t*t
        L.append(f"2^{2**(i+1)}")
    print(L)
    print([L[i] for i in p])

exp_by_squaring_example(2,471)



#inds = binary_partition(471)
#
#L = ["2"]
#for i in range(inds[-1]):
#    L.append(f"2^{2**i}")
#
#print(L)
#print([L[i] for i in inds])
#
#
#print(exp_by_squaring(2,471))