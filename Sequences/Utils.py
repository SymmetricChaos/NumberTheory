# Skip the first few values of a sequence
def offset(sequence,offset=0,**kwargs):
    if type(offset) != int:
        raise Exception("offset must be an integer")
        
    if offset < 0:
        raise Exception("offset must be nonnegative")
        
    for ctr,val in enumerate(sequence(**kwargs)):
          
        if ctr >= offset:
            yield val 

# Return some number of values with some offset
def partial(sequence,num_vals=0,offset=0,**kwargs):

    if type(num_vals) != int:
        raise Exception("n_vals must be an integer")
    if type(offset) != int:
        raise Exception("offset must be an integer")
            
    if num_vals < 0:
        raise Exception("n_vals must be nonnegative")
    if offset < 0:
        raise Exception("offset must be nonnegative")
    
    if num_vals == 0:
        num_vals = float('inf')
    
    for ctr,val in enumerate(sequence(**kwargs)):
        if ctr >= num_vals+offset:
            break
          
        if ctr >= offset:
            yield val
            
 

        
def seq_max(sequence,max_val=None,**kwargs):

    if type(max_val) != int and type(max_val) != None:
        raise Exception("offset must be an integer or infinite")
    
    if max_val == None:
        max_val = float("inf")
    
    for val in sequence(**kwargs):
        yield val          
        if val > max_val:
            break

def show_vals(sequence,**kwargs):
    
    print(sequence.__doc__,end="")
    
    if kwargs == {}:
        print()
    else:
        print(":",end=" ")
        for i,j in kwargs.items():
            print("{} = {}".format(i,j),end="  ")
        print()
        
    part = partial(sequence,20,**kwargs)
    
    L = []
    
    for i in part:
        if i > 1000:
            break
        L.append(i)
        
    print(*L,sep=", ")
        
    print("\n")



# Legacy of a more complicated method
        
#def sequence_maker(generator):
#    
#    def S(num_vals=0,offset=0,**kwargs):
#        
#        sequence_params(num_vals, offset)
#                
#        if num_vals == 0:
#            num_vals = float('inf')
#            
#        for ctr,val in enumerate(generator(**kwargs)):
#            if ctr >= num_vals+offset:
#                break
#            
#            if ctr >= offset:
#                yield val
#    S.__name__ = generator.__name__
#    return S