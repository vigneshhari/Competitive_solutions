looped = []

class graph:
    def __init__(self):
        self.neighbors = {}

    def add_vertex(self, v):
        if v not in self.neighbors:
            self.neighbors[v] = []

    def add_edge(self, u, v):
        self.neighbors[u].append(v)
        # if u == v, do not connect u to itself twice
        if u != v:
            self.neighbors[v].append(u)

    def vertices(self):
        return list(self.neighbors.keys())

    def vertex_neighbors(self, v):
        return self.neighbors[v]

def is_cyclic_graph(G):
    Q = []
    V = G.vertices()

    layer = {v: -1 for v in V}

    for v in V:
        layer = {v: -1 for v in V}
        # v has already been explored; move on
        if layer[v] != -1:
            continue

        # take v as a starting vertex
        layer[v] = 0
        Q.append(v)

        # as long as Q is not empty
        while len(Q) > 0:

            # get the next vertex u of Q that must be looked at
            u = Q.pop(0)

            C = G.vertex_neighbors(u)
            for z in C:
                # if z is being found for the first time
                if layer[z] == -1:
                    layer[z] = layer[u] + 1
                    Q.append(z)
                elif layer[z] >= layer[u]:
                    looped.append(z)





maxval , no = map(int , raw_input().split(" "))

g = graph()

for i in range(1,no+1):
    g.add_vertex(i)

for i in range(no):
    a,b = map(int , raw_input().split(" "))
    g.add_edge(a,b)

is_cyclic_graph(g)

val = set(range(1,no)) - set(looped)

for i in val :print i
