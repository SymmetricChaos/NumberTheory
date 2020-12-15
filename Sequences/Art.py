from Sequences import Drawing as draw
from Sequences import primitive_pythagorean_triples
import numpy as np


def centered_figurate(k,n):
    """
    Show the first n centered k-gonal numbers
    """
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    
    draw.circle_xy(0,0,.1)
    
    th = np.linspace(0,2*np.pi,k+1)
    
    for i in range(1,n):
        x = np.sin(th[:k])*(3.5*i/(n-1))
        y = np.cos(th[:k])*(3.5*i/(n-1))
        
        for p in range(k):
            x_space = np.linspace(x[p%k],x[(p+1)%k],i+1)
            y_space = np.linspace(y[p%k],y[(p+1)%k],i+1)
            draw.circles_xy(x_space,y_space,[.1]*(i+1))


def figurate(k,n):
    """
    Show the first n ordinary k-gonal numbers
    """
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    
    draw.circle_xy(0,3.5,.1)
    
    th = np.linspace(0,2*np.pi,k+1)
    
    for i in range(1,n):
        x = np.sin(th[:k])*(3.5*i/(n-1))
        y = np.cos(th[:k])*(3.5*i/(n-1))+3.5-3.5*i/(n-1)
        
        for p in range(k):
            x_space = np.linspace(x[p%k],x[(p+1)%k],i+1)
            y_space = np.linspace(y[p%k],y[(p+1)%k],i+1)
            draw.circles_xy(x_space,y_space,[.1]*(i+1))


def show_primitive_pthyagorean_triples(n):
    """
    Plot out the primitive integer right triangles with hypotenuse less than or equal n
    """
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-.5,n],[-.5,n])
    
    for T in primitive_pythagorean_triples():
        if T[2] > n:
            break
        
        pt1 = (0,0)
        pt2 = (T[2],0)
        pt3 = (T[2],T[1])
        
        draw.connection_p(pt1,pt2,alpha=.2)
        draw.connection_p(pt2,pt3,alpha=.2)
        draw.connection_p(pt3,pt1,alpha=.2)


def sum_of_triangular(n):
    """
    Show why the sums of consecutive triangular numbers are square
    """


# centered_figurate(5,5)
# figurate(5,5)
show_primitive_pthyagorean_triples(100)