from Sequences import Drawing as draw
import numpy as np


def centered_figurate(k,n):
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    
    draw.circle_xy(0,0,.1)
    
    th = np.linspace(0,2*np.pi,k+1)
    
    for i in range(1,n+1):
        x = np.sin(th[:k])*(3.5*i/n)
        y = np.cos(th[:k])*(3.5*i/n)
        
        for p in range(k):
            x_space = np.linspace(x[p%k],x[(p+1)%k],i+1)
            y_space = np.linspace(y[p%k],y[(p+1)%k],i+1)
            draw.circles_xy(x_space,y_space,[.1]*(i+1))


def figurate(k,n):
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    
    draw.circle_xy(0,3.5,.1)
    
    th = np.linspace(0,2*np.pi,k+1)
    
    for i in range(1,n+1):
        x = np.sin(th[:k])*(3.5*i/n)
        y = np.cos(th[:k])*(3.5*i/n)+3.5-3.5*i/n
        
        for p in range(k):
            x_space = np.linspace(x[p%k],x[(p+1)%k],i+1)
            y_space = np.linspace(y[p%k],y[(p+1)%k],i+1)
            draw.circles_xy(x_space,y_space,[.1]*(i+1))



centered_figurate(5,4)
figurate(5,4)