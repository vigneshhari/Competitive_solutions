#Code Chef Problem RRFRNDS


class Graph:
 
    def __init__(self,vertices):
        self.graph = {}
        for i in range(vertices):
            self.graph[i] = [i]

    def addedge(self,u,v):
        self.graph[u] = self.graph[u] + [v]

    def closure(self,u):
        out = []
        for i in self.graph[u]:
            out += self.graph[i]
        return out

    def max_friends(self,i):
        return len(set(self.closure(i)) - set(self.graph[i])) 

#temp = [map(int , list(i)) for i in  test.split("\n")]

people = input()
temp = []
for i in range(people):
    temp.append(list(raw_input()))

g = Graph(people)

for i in range(people):
    for j in range(people):
        if(temp[i][j] == "1"):g.addedge(i,j)

out = 0
for i in g.graph.keys():
    out += g.max_friends(i)

print out