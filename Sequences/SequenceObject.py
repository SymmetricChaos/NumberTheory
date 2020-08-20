from Sequences.NiceErrorChecking import require_iterable, require_callable

# Sequence object with slightly more functional behavior. Specifically it is
# not a generator. If a Sequence is created it uses a new generator each time
# it is called
# Maybe useful

class Sequence:
    
    def __init__(self,sequence,index=None):
        
        require_callable(["sequence"],[sequence])
        require_iterable(["sequence()"],[sequence()])
        
        self.sequence = sequence
        self.index = index
    
    
    def __call__(self,*args,**kwargs):
        for i in self.sequence(*args,**kwargs):
            yield i