from Sequences import Drawing as draw
import numpy as np
from Sequences.Combinatorics import motzkin_paths, dyck_words, catalan, pascal_triangle
from Sequences.Manipulations import segment
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


def pascal_triangle_art(n,circle_size=.13,circle_color="lavender",cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title("Pascal's Triangle",size=30)
    
    draw.text_xy(0,2.5,"1",ha='center',va='center')
    draw.circle_xy(0,2.5,circle_size,fc=circle_color)
    
    for k,row in enumerate(segment(pascal_triangle(),1),1):
        y = 2.5-3.5*k/n
        x_space = np.linspace(-3.5*k/n,3.5*k/n,k+1)
        
        for x,val in zip(x_space,row):
            draw.circle_xy(x,y,circle_size,fc=circle_color)
            draw.text_xy(x,y,val,ha='center',va='center')
        if k >= n:
            break



# def dyck_paths(n):
    


# dyck_mountains(5)
# motzkin_mountains(5)
pascal_triangle_art(12)