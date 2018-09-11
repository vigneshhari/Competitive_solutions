class Graph:

    removed = []
    groups = {}
    max_group = 1
    def __init__(self, n):
        self.graph = {}
        self.distmatrix = {}
        for i in xrange(n+1):
            self.groups[i] = 1

    def addedge(self,u,v):
        self.graph[u] = self.graph.get(u,[]) +  [v]
        self.graph[v] = self.graph.get(v,[]) +  [u]

    def removeedge(self,u,v):
        if(u in self.graph[v]):
            del self.graph[u][self.graph[u].index(v)]
            del self.graph[v][self.graph[v].index(u)]
        self.removed.append((u,v))
        self.normal_bfs(u,self.max_group+1)
        self.normal_bfs(v,self.max_group+2)
        self.max_group+=2

    def distancefinder(self,u,v):
        if(self.groups[u] != self.groups[v]):return "Impossible"
        return self.bfs_finder(u,v)
    

    def addoldedge(self,u,v):
        if((u,v) in self.removed ):
            self.graph[u] = self.graph.get(u,[]) +  [v]
            self.graph[v] = self.graph.get(v,[]) +  [u]
            del self.removed[ self.removed.index((u,v)) ]
            self.normal_bfs(u,self.max_group+1)
            self.max_group+=1
        elif((v,u) in self.removed):
            self.graph[u] = self.graph.get(u,[]) +  [v]
            self.graph[v] = self.graph.get(v,[]) +  [u]
            del self.removed[ self.removed.index((v,u)) ]
            self.normal_bfs(u,self.max_group+1)
            self.max_group+=1
        


    def bfs_finder(self,starter,end):
        stack = [(starter,0)]
        pos = 0
        out = []
        visited = []
        while stack != []:
            pos = stack[0][0]
            level = stack[0][1] + 1
            out.append(stack[0])
            visited.append(pos)
            del stack[0]
            for i in self.graph[pos]:
                if(i not in visited):
                    if(i == end):
                        return level
                    stack.append((i,level))
    
    def normal_bfs(self,starter,group):
        stack = [starter]
        pos = 0
        out = []
        while stack != []:
            pos = stack[0]
            self.groups[pos] = group
            out.append(pos)
            del stack[0]
            for i in self.graph[pos]:
                if(i not in out):
                    stack.append(i)


nodes = input()
g = Graph(nodes)
for i in xrange(nodes - 1):
    u,v = map(int , raw_input().split())
    g.addedge(u,v)

queries = input()
for i in xrange(queries):
    q = raw_input().split()
    if(q[0] == "q"):
        print g.distancefinder(int(q[1]),int(q[2]))
    elif(q[0] == "d"):
        g.removeedge(int(q[1]),int(q[2]))
    elif(q[0] == "c"):
        g.addoldedge(int(q[1]),int(q[2]))
