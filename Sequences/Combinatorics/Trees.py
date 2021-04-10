

def max_tree_nodes(m=2):
    """
    Maximum number of nodes in an m-tree of height n
    """
    
    s = 1
    p = m
    
    while True:
        yield s
        s += p
        p *= m







if __name__ == '__main__':
    from Sequences.Manipulations import simple_test
    
    print("\nNumber of Nodes in a Full Ternary Tree")
    simple_test(max_tree_nodes(3),10,
                "1, 4, 13, 40, 121, 364, 1093, 3280, 9841, 29524")
    