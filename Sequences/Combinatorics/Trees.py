from math import comb
from Sequences.Simple import naturals

def max_tree_nodes(k=2):
    """
    Maximum number of nodes in an k-ary tree of height n
    OEIS
    """
    
    s = 1
    p = k
    
    while True:
        yield s
        s += p
        p *= k


def free_tree():
    """
    Number of unique free trees with n unlabeled nodes
    OEIS A000055
    """
    
    


def rooted_tree():
    """
    Number of unique rooted trees with n unlabeled nodes
    OEIS A000081
    """
    




def oriented_tree():
    """
    Number of unique oriented trees with n unlabeled nodes
    OEIS A000238
    """
    
    # a(n+1) = (1/n) * Sum_{k=1..n} ( Sum_{d|k} d*a(d) ) * a(n-k+1).
    
    
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


def ordered_tree():
    """
    Number of unique ordered trees with n unlabeled nodes
    OEIS 
    """




if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nNumber of Nodes in a Full Ternary Tree")
    simple_test(max_tree_nodes(3),10,
                "1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524")
    
    print("\nNumber of unique oriented trees with n unlabeled nodes")
    simple_test(oriented_tree(),12,
                "0, 1, 1, 2, 4, 9, 20, 48, 115, 286, 719, 1842")
    