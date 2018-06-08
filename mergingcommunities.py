class Size_Set:

    def __init__(self,size):
        self.Makeset(size)
    
    def Makeset(self,size):
        self.S = [-1 ] * (size+2)
    
    def Find(self,x):
        if(self.S[x] < 0):
            return x
        else:
            return self.Find(self.S[x])
    

    def Union(self,root1,root2):
        if(self.Find(root1) == self.Find(root2) and self.Find(root1) == -1):return
        if(self.S[root2] < self.S[root1]):
            self.S[root2] += self.S[root1]
            self.S[root1] = root2 
        else:
            self.S[root1] += self.S[root2]
            self.S[root2] = root1


n ,q = map(int , raw_input().split())
comm = Size_Set(n)
for _ in xrange(q):
    inp = raw_input().split()
    if(inp[0] == "Q"):
        print -1 * comm.S[comm.Find(int(inp[1]))]
    else:
        comm.Union(int(inp[1]) , int(inp[2]))
