import numpy as np
from GeneralUtils import list_to_sum

class Fourier:
    
    def __init__(self,amp=[1],freq=[1],ph=[0]):
        self.amp = amp
        self.freq = freq
        self.ph = ph
        
    def __str__(self):
        out = []
        for i in range(len(self.amp)):
            if self.amp[i] != 1:
                a = f"{self.amp[i]}*"
            else:
                a = ""
                
            if self.freq[i] != 1:
                f = f"*{self.freq[i]}"
            else:
                f = ""
                
            if self.ph[i] != 0:
                p = f"+{self.ph[i]}"
            else:
                p = ""
                
            out.append(f"{a}sin(x{f}{p})")
            
        return list_to_sum(out)
    
    def __add__(self,other):
        a = self.amp + other.amp
        f = self.freq + other.freq
        p = self.ph + other.ph
        return Fourier(a,f,p)

        
def evaluate_series(F,x):
    out = np.zeros_like(x)
    for i in range(len(F.amp)):
        a = F.amp[i]
        f = F.freq[i]
        p = F.ph[i]
        out += a*np.sin(x*f+p)
    return out

