

class GraphWeighted:

    def __init__(self, directed = 0 , edges = {} ):
        self.edges = edges
        self.directed = directed
    
    def addedge(self , a , b , cost):
        a,b = map(str , (a,b))
        self.edges[a] = self.edges.get(a , []) + [(b,cost)]
        if(self.directed == 0):
            self.edges[b] = self.edges(b,[]) + [(a,cost)]
    
    def __str__(self):
        return str(self.edges)