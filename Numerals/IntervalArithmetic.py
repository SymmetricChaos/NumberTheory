class IntervalNum:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
        
    def __str__(self):
        return f"[{self.a};{self.b}]"
    
    
    def __add__(self,other):
        return IntervalNum(self.a+other.a, self.b+other.b)
    
    
    def __sub__(self,other):
        return IntervalNum(self.a-other.b, self.b-other.a)



if __name__ == '__main__':
    x = IntervalNum(2,3)
    print(f"x = {x}")
    print(f"x+x = {x+x}")
    print(f"x-x = {x-x}")