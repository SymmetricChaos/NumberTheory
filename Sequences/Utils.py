def partial(sequence,num_vals=0,offset=0,**kwargs):

    if type(num_vals) != int:
        raise Exception("n_vals must be an integer")
    if type(offset) != int:
        raise Exception("offset must be an integer")
            
    if num_vals < 0:
        raise Exception("n_vals must be nonnegative")
    if offset < 0:
        raise Exception("offset must ber nonnegative")
    
    if offset > num_vals:
        raise Exception("offset cannot be greater than num_vals")
            
    for ctr,val in enumerate(sequence(**kwargs)):
        if ctr >= num_vals+offset:
            break
          
        if ctr >= offset:
            yield val
            
def min_max(sequence,min_val=None,max_val=None,**kwargs):

    if type(min_val) != int and type(min_val) != None:
        raise Exception("n_vals must be an integer or infinite")
    if type(max_val) != int and type(max_val) != None:
        raise Exception("offset must be an integer or infinite")
    
    if min_val == None:
        min_val = float("-inf")
    
    if max_val == None:
        max_val = float("inf")
    
    if min_val > max_val:
        raise Exception("min_val cannot be greather than max_val")
        
    for val in sequence(**kwargs):
        if val >= min_val:
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