from Sequences import Drawing as draw
import numpy as np


def centered_triangular(n):
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-3.5,4.5])
    
    draw.circle_xy(0,0,.1)
    
    th = np.linspace(0,2*np.pi,4)
    
    for i in range(1,n+1):
        x = np.sin(th[:3])*(4*i/n)
        y = np.cos(th[:3])*(4*i/n)
        
        for p in range(3):
            x_space = np.linspace(x[p%3],x[(p+1)%3],i+1)
            y_space = np.linspace(y[p%3],y[(p+1)%3],i+1)
            draw.circles_xy(x_space,y_space,[.1]*(i+1))

centered_triangular(7)