from collections import defaultdict

looped = []

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)



    def Checker(self , listvertex ,visited, pvertex,level):
        for i in listvertex:
            if(i == pvertex ):looped.append(level);return
            if(i in visited): continue
            visited.append(i)
            self.Checker(self.graph[i],visited[:],pvertex,level + 1)
        return False

    def CheckCycle(self,vertex):
        return self.Checker(self.graph[vertex] , [vertex] , vertex,1)


maxval , no = map(int , raw_input().split(" "))

g = Graph(no)

for i in range(no):
    a,b = map(int , raw_input().split(" "))
    g.addEdge(a, b)

for i in range(1,maxval+1):
    g.CheckCycle(i)


out =  set(range(1,maxval+1)) - set(looped)