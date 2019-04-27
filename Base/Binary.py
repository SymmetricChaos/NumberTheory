from Base.BaseConvert import base_convert

class Binary:
    
    def __init__(self,number):
        assert type(number) == int
        self.digits = base_convert(number,2)
    
    def __str__(self):
        return "".join([str(d) for d in self.digits])
    
    def __repr__(self):
        return "".join([str(d) for d in self.digits])


def half_adder(a,b):
    """Single bit addition"""
    return (a+b)%2

def full_adder(a,b,c=0):
    """Single bit addition with carry"""
    s = (a+b+c)%2
    cout = a*b + (c*(a+b)%2)
    return s,cout



for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print(x,y,z,full_adder(x,y,z))