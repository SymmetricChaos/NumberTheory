class Graph:
    """Undirected Graph"""
    
    def __init__(self,n):
        """Make a graph with n nodes"""
        self.nodes = []
        for i in range(n):
            self.nodes.append({})

    def add_edge(self,a,b,d=1):
        """Add an edge from node a to node b with length d"""
        self.nodes[a].update({b:d})
        self.nodes[b].update({a:d})
    
    def add_node(self,n):
        """Add a node"""
        for i in range(n):
            self.nodes.append({})

    def __str__(self):
        s = ""
        for p,n in enumerate(self.nodes):
            s += f"{p} {n}\n"
        return s
                
class DirGraph:
    """Directed Graph"""
    
    def __init__(self,n):
        """Make a directed graph with n nodes"""
        self.nodes = []
        for i in range(n):
            self.nodes.append({})

    def add_edge(self,a,b,d=1):
        """Add a directed edge from node a to node b with length d"""
        self.nodes[a].update({b:d})
    
    def add_node(self,n):
        """Add a node"""
        for i in range(n):
            self.nodes.append({})
