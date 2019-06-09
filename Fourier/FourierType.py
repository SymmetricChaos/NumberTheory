from math import sin

class Fourier:
    
    def __init__(self,amp,freq,ph):
        self.amp = amp
        self.freq = freq
        self.ph = ph
    

    def evaluate(self,x):
        L = []
        if type(x) == list:
            for i in x:
                L.append(amp*sin(i*ph)+ph)
        return amp*sin(x*ph)+ph
    
    def __add__(self,other):
        