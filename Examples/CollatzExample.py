from Sequences import collatz_numbers

print("Length of the Collatz Sequence at Each Number\n")
for n,val in enumerate(collatz_numbers(),1):
    print(f"{n:<2} = {val}")
    if n > 20:
        break


print("\n\nHigh Water Marks of the Collatz Sequence\n")    
m = 0
print("1   = 0")
for n,val in enumerate(collatz_numbers(),1):
    if val > m:
        print(f"{n:<3} = {val}")
        m = val
    if n > 1000:
        break