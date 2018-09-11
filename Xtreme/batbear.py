from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)


    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True

            elif parent != i:
                return True

        return False

    def isCyclic(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False


inp = input()
for i in range(inp):
    lim , gnodes = map(int , raw_input().split(" "))
    g = Graph(lim)
    nodes = map(int , raw_input().split(" "))
    while nodes != []:
        g.addEdge(nodes[0],nodes[1])
        del nodes[0:2]
    if(g.isCyclic()):print"1"
    else:print "0"