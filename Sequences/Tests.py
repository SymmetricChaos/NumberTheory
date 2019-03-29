from Sequences import *


for seq in [naturals,integers,fibonacci,lucas]:
    print(seq.__name__)
    for i in seq.values(10):
        print(i)
    print()