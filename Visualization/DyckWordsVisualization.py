from Combinatorics import dyck_words
import matplotlib.pyplot as plt

N = 5
D = dyck_words(N)
h = len(D)//5+1

fig1, axs = plt.subplots(h, 5, figsize=(13, h*2.5))
word = 0
for ax in axs:
    for a in ax:
        a.set_axis_off()
        a.set_ylim([-.5, N])
        x = [i for i in range(2*N+1)]
        y = [0]*len(x)
        if word > len(D)-1:
            continue
        else:
            for ctr,i in enumerate(D[word],1):
                if i == "(":
                    y[ctr] = y[ctr-1]+1
                if i == ")":
                    y[ctr] = y[ctr-1]-1
            a.plot(x,y)
            a.bar(x,y,width=.1)
            word += 1