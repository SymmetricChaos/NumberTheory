from Sequences import Drawing as draw
from Sequences.Combinatorics import motzkin_paths, dyck_words, catalan, pascal_triangle, motzkin_chords, partitions

import numpy as np
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


def pascal_triangle_art(n,circle_size=.15,text_size=8,circle_color="lavender",cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title("Pascal's Triangle",size=30)
    
    for k,row in enumerate(pascal_triangle(),0):
        y = 2.5-4*k/n
        x_space = np.linspace(-3.7*k/n,3.7*k/n,k+1)
        
        for x,val in zip(x_space,row):
            draw.circle_xy(x,y,circle_size,fc=circle_color)
            draw.text_xy(x,y,val,ha='center',va='center',size=text_size)
        if k >= n:
            break


def pascal_sierpinski_art(n,circle_size=.12,text_size=8,circle_color="cornflowerblue",cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title("Sierpinski Triangle\nBuilt From Pascal's Triangle",size=30)
    
    for k,row in enumerate(pascal_triangle(),0):
        y = 2.5-4*k/n
        x_space = np.linspace(-3.7*k/n,3.7*k/n,k+1)
        
        for x,val in zip(x_space,row):
            if val % 2 == 1:
                draw.circle_xy(x,y,circle_size,fc=circle_color)
            else:
                draw.circle_xy(x,y,circle_size,fc="white",ec="black")
            draw.text_xy(x,y,val,ha='center',va='center',size=text_size)
        if k >= n:
            break


# Each chord partitions the set of points into three sets: those on the chord, those to the "left", and those to the "right"
# We generate solutions by using this knowledge to then partition each partition
def motzkin_chords_art(n,cavas_size=[15,15],rows=10,cols=10):
    
    draw.make_blank_canvas(cavas_size,facecolor="lightgray")
    
    th = np.linspace(0,2*np.pi,n+1)
    x = np.sin(th[:n])
    y = np.cos(th[:n])
    P = draw.xy_to_points(x,y)
    
    for ctr,i in enumerate(motzkin_chords(n),1):
        draw.make_blank_plot(rows,cols,ctr,[-1.2,1.2],[-1.2,1.2])
        draw.circle_xy(0, 0, 1, fc='white', ec='black',zorder=-1)
        for pair in i:
            draw.connection_p(P[pair[0]],P[pair[1]],color='red',zorder=0)
        draw.circles_xy(x,y,[.1]*n)


def partition_art(n,cavas_size=[15,15]):
    
    draw.make_blank_canvas(cavas_size,facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title(f"Partitions of {n}",size=30)
    
    parts = [i for i in partitions(n)]
    
    xunit = 7/n
    yunit = 7/len(parts)
    
    y = -3.5
    
    for p in parts:
        x = -3.5
        
        for section in p:
            draw.rect_xy(x, y, x+section*xunit, y+yunit,facecolor="salmon",edgecolor="black",lw=3)
            x += section*xunit
        
        y += yunit





# dyck_mountains(5)
# motzkin_mountains(5)
# pascal_triangle_art(14)
# pascal_sierpinski_art(15)
# motzkin_chords_art(6,rows=8,cols=8)
partition_art(9)