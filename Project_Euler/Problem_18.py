
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


# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
import sys  # Library for INT_MAX
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    
    def addedge(self,u,v,w):
        self.graph[u][v] = w

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print "Edge \tWeight"
        for i in range(1,self.V):
            print parent[i],"-",i,"\t",self.graph[i][ parent[i] ]
 
    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initilaize min value
        min = sys.maxint
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def primMST(self):
 
        #Key values used to pick minimum weight edge in cut
        key = [sys.maxint] * self.V
        parent = [None] * self.V # Array to store constructed MST
        key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V
 
        parent[0] = -1  # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)
# Driver code

mapover = {0:0}
def mapper(val):
    pos = max(mapover.keys()) + 1
    mapover[pos] = val
    return pos

cleantree = [map(int , i.split()) for i in tree.split("\n")]

newtree = [ [ mapper(i) for i in j  ] for j in cleantree ]


g = Graph(max(mapover.keys()) + 1)

stack = [(0,0)]

while True:
    if(stack == []):break
    current = newtree[stack[0][0]][stack[0][1]]
    newv = newtree[stack[0][0] + 1][stack[0][1]]
    g.addedge(current , newv , mapover[newv]  )
    newv = newtree[stack[0][0] + 1][stack[0][1] + 1]
    g.addedge(current , newv , mapover[newv]  )
    if(stack[0][0]  < (len(newtree) - 2)):
        stack.append( (stack[0][0] + 1 , stack[0][1] ) )
        stack.append( (stack[0][0] + 1 , stack[0][1] + 1 ) )
    del stack[0]

print g.graph

g.primMST()
    
 
