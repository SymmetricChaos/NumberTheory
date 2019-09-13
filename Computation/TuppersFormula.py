from math import floor
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

    
def tupper(x,y,h=17):
    x = Fraction(x)
    y = Fraction(y)
    a = y//h
    b = (-h*x)-(y%h)
    fin = (a*2**b)%2
    if floor(fin) < .5:
        return 1
    else:
        return 0
    



Ymin = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
Yheight = 17
X = 107
G = np.zeros((X,Yheight),dtype=int)

for x in range(X):
    for y in range(Yheight):
        G[x,y] = tupper(x,Ymin+y)

G = np.flip(G,0).T

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(5,5)

plt.imshow(G, interpolation='none')