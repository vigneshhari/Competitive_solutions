tree = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""



class Graph:
 
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = []
  
    def addedge(self,u,v,w):
        if([u,v,w] not in self.graph):
            self.graph.append([u, v, w])
         

    def solve(self, src): # Varient of BellMan Ford Algo

        dist = [0] * self.V
        dist[src] = 0
 
        for i in range(self.V - 1):
            change = True
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        change = False

            if(change):break
                
        print min(dist) * -1

mapover = {0:0}
def mapper(val):
    pos = max(mapover.keys()) + 1
    mapover[pos] = val
    return pos

cleantree = [map(int , i.split()) for i in tree.split("\n")]

cleantree[1][0] += cleantree[0][0]
cleantree[1][1] += cleantree[0][0] 

newtree = [ [ mapper(i) for i in j  ] for j in cleantree ]

g = Graph(max(mapover.keys()) + 1)
root = g
stack = [(0,0)]

for i in range(len(newtree) -1):
    for m in range(i + 1):
        g.addedge(newtree[i][m] , newtree[i+1][m] , -1 *mapover[newtree[i+1][m]])
        g.addedge(newtree[i][m] , newtree[i+1][m+1] , -1 *mapover[newtree[i+1][m+1]])

g.solve(1)
    
 
