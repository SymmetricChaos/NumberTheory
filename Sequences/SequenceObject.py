# Sequence object with slightly more functional behavior
# Maybe useful

class Sequence:
    
    def __init__(self,sequence,index=None):
        
        if not callable(sequence):
            raise Exception("Sequence should be a function")
        if not iter(sequence()):
            raise Exception("Sequence must be an iterator when called")
        
        self.sequence = sequence
        self.index = index
    
    
    def __call__(self,*args,**kwargs):
        for i in self.sequence(*args,**kwargs):
            yield i

