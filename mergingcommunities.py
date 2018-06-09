class Size_Set:
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n

    def _root(self, i):
        j = i
        while (j != self._id[j]):
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def Find(self, p, q):
        return self._root(p) == self._root(q)
    
    def Union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if (self._sz[i] < self._sz[j]):
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]


n ,q = map(int , raw_input().split())
comm = Size_Set(n)
for _ in xrange(q):
    inp = raw_input().split()
    if(inp[0] == "Q"):
        print  comm._sz[comm._id[int(inp[1])]]
    else:
        comm.Union(int(inp[1]) , int(inp[2]))

'''
10 10
M 1 2
M 1 3
M 10 9
M 10 1
M 5 7
M 10 2
Q 2
'''