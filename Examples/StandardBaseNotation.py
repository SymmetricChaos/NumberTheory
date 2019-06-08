from Computation import base_convert

print("     ","B2".rjust(5),"B3".rjust(5),"B4".rjust(5),"B5".rjust(5))
for i in range(32):
    t1 = "".join(str(x) for x in base_convert(i,2))
    t2 = "".join(str(x) for x in base_convert(i,3))
    t3 = "".join(str(x) for x in base_convert(i,4))
    t4 = "".join(str(x) for x in base_convert(i,5))
    t = "{}:".format(i)
    print(t.ljust(5),t1.rjust(5),t2.rjust(5),t3.rjust(5),t4.rjust(5))
    
