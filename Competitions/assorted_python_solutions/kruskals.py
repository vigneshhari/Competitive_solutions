

from collections import defaultdict
import operator

class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
        self.weight = {}
 
  
    def addEdge(self,v,w,weight):
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.weight[(v,w)] = weight

    def removeEdge(self,v,w,weight):
        del self.graph[v][self.graph[v].index(w)]
        del self.graph[w][self.graph[w].index(v)]
        del self.weight[(v,w)]

    def isCyclicUtil(self,v,visited,parent):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            elif parent!=i:
                return True
        return False
        
    def isCyclic(self):
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i] ==False: 
                if(self.isCyclicUtil(i,visited,-1))== True:
                    return True
        return False

nn , q = map(int , raw_input().split(" "))
g = Graph(nn)
for i in range(q):
    a,b,c = map(int , raw_input().split(" "))
    g.addEdge(a-1,b-1,c)

ng = Graph(nn)

ls = sorted(g.weight.items(), key=operator.itemgetter(1))
while True: 
    for i in sorted(g.weight.items(), key=operator.itemgetter(0)):
        if(len(ls) == 0 ):break    
        if(i[1] == ls[0][1]):
            ng.addEdge(i[0][0] , i[0][1] , i[1] )
            if ng.isCyclic():
                ng.removeEdge(i[0][0] , i[0][1] , i[1])
                g.removeEdge(i[0][0] , i[0][1] , i[1])     
            del ls[0]
            break
    if(len(ls) == 0 ):break    

sum = 0

for i in ng.weight.keys():
    sum+=ng.weight[i]

print sum