
class Graph:

    def __init__(self  , directed = 0 , edges = {}): # 1 is directed , 0 is undirected
        self.edges = edges
        self.directed = directed

    def addedge(self,a,b):
        a,b = map(str , (a,b))
        if(self.directed):
            self.edges[a] = self.edges.get(a,[]) + list(b)
        else:
            self.edges[a] = self.edges.get(a,[]) + list(b)
            self.edges[b] = self.edges.get(b,[]) + list(a)
    
    def DFS(self,start):
        out = [start]
        checker = self.edges.get(str(start) , [])
        while checker != []:
            current = checker[-1]
            del checker[-1]
            if(current in out):continue
            newedges = self.edges.get(str(current) , [])
            out.append(current)
            checker += newedges
        return out

    def BFS(self,start):
        out = [str(start)]
        checker = self.edges.get(str(start) , [])
        while checker != []:
            current = checker[0]
            del checker[0]
            if(current in out):continue
            newedges = self.edges.get(str(current) , [])
            out.append(current)
            checker += newedges
        return out

    def __str__(self):
        return str(self.edges)