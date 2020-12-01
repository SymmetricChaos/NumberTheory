from Sequences import Drawing as draw
import numpy as np
from Sequences.Combinatorics import motzkin_paths, dyck_words, catalan
from math import comb


def dyck_mountains(n=2):
    
    num_words = comb(2*n,n)//(n+1)
    
    size = 1
    while size*size < num_words:
        size += 1
    
    W = dyck_words(n)
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    
    for pos,word in enumerate(W,1):
        draw.make_blank_plot(size,size,pos,[-4,4])
        x = -4
        y = -4
        for move in word:
            draw.connection_p((x,y),(x+(4/n),y+(4/n)*move))
            x = x+(4/n)
            y = y+(4/n)*move


def motzkin_mountains(n=2):
    
    num_words = sum([comb(n,2*k)*c for k,c in zip(range(0,n//2+1),catalan())])
    print(num_words)
    
    size = 1
    while size*size < num_words:
        size += 1
    
    W = motzkin_paths(n)
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    
    for pos,word in enumerate(W,1):
        draw.make_blank_plot(size,size,pos,[-4,4])
        x = -4
        y = -3.95
        for move in word:
            draw.connection_p((x,y),(x+(8/n),y+(8/n)*move))
            x = x+(8/n)
            y = y+(8/n)*move

dyck_mountains(5)
motzkin_mountains(5)