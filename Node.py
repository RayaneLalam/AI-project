class Node:
    
    def __init__(self, state, parent=None, action=None, cost=0, estimatedCost=0):
        self.state = state
        self.parent = parent # node
        self.action = action # action performed to get to this node
        self.cost = cost # (incremented with each newly expanded node)
        self.estimatedCost = estimatedCost
        if parent is None: # root node
            self.depth = 0 # level in the graph 0 for the root node
        else:
            self.depth = parent.depth + 1 # parent level + 1
            
            
    def getPath(self):
        path = [self]
        while self.parent != None:
            path.append(self.parent)
            self = self.parent
        return path
        
            
        
    def __hash__(self):
        if isinstance(self.state, list):
            return hash((tuple(map(tuple, self.state))))
        else:
            return hash(self.state)
        
        
    #__eq__ overloads the = operator    
    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
    
    
    def __gt__(self, other): #greater than operator
        return isinstance(other, Node) and self.cost + self.estimatedCost > other.cost + other.estimatedCost


    def __lt__(self, other):
        return isinstance(other, Node) and self.cost + self.estimatedCost < other.cost + other.estimatedCost
        
        
        
        
        
        
        
        
        
        
        