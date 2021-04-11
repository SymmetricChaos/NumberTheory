from Sequences.Simple import naturals

def max_tree_nodes(k=2):
    """
    Maximum number of nodes in an k-ary tree of height n
    OEIS A000225, A003462, A002450, A003463, A003464
    """
    
    s = 1
    p = k
    
    while True:
        yield s
        s += p
        p *= k


def binary_tree():
    """
    Number of binary trees of height n
    OEIS A001699
    """
    
    yield 1
    yield 1
    
    s = 1 # sum of previous terms
    c = 1 # current value
    p = 1 # previous value
    
    while True:
        c = 2*c*s+(c*c)
        s += p
        p = c
        yield c





def rooted_tree():
    """
    Number of unique rooted trees with n unlabeled nodes
    OEIS A000081
    """
    
    A = [0,1]
    
    yield from A
    
    for n in naturals(1):
        out = 0
        for k in range(1,n+1):
            d_sum = 0
            for d in range(1,k+1):
                if k%d == 0:
                    d_sum += d*A[d]
            d_sum *= A[n-k+1]
            out += d_sum
        
        A.append(out//n)
        yield out//n





def oriented_tree():
    """
    Number of unique oriented trees with n unlabeled nodes
    OEIS A000238
    """
    
    


def ordered_tree():
    """
    Number of unique ordered trees with n unlabeled nodes
    OEIS 
    """
    


def free_tree():
    """
    Number of unique free trees with n unlabeled nodes
    OEIS A000055
    """
    





if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nNumber of Nodes in a Full Ternary Tree")
    simple_test(max_tree_nodes(3),10,
                "1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524")
    
    print("\nNumber of unique oriented trees with n unlabeled nodes")
    simple_test(rooted_tree(),12,
                "0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842")
    
    print("\nNumber Binary Trees of Height n")
    simple_test(binary_tree(),7,
                "1, 1, 3, 21, 651, 457653, 210065930571")
    