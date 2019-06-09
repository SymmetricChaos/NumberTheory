import numpy as np

class Fourier:
    
    def __init__(self,amp,freq,ph):
        self.amp = amp
        self.freq = freq
        self.ph = ph
        
    
    def __add__(self,other):
        a = self.amp + other.amp
        f = self.freq + other.freq
        p = self.ph + other.ph
        return Fourier(a,f,p)
        
        
def evaluate_series(F,x):
    out = np.zeros_like(x)
    print(F.amp)
    for i in range(len(F.amp)):
        a = F.amp[i]
        f = F.freq[i]
        p = F.ph[i]
        out += a*np.sin(x*f+p)
    return out

