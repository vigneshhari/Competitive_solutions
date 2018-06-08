class Size_Set:

    def __init__(self,size):
        self.ds = [ [i] for i in xrange(size+1) ]

    def Union(self,e1 , e2):
        e1 = self.Find(e1)
        e2 = self.Find(e2)
        if(e1 == e2):return 
        l1  = self.ds[e1]
        l2 = self.ds[e2]
        if(len(l1) > len(l2)):
            self.ds[e1] = self.ds[e1] +  self.ds[e2]
            for i in self.ds[e2]:
                self.ds[i] = e1
        else:
            self.ds[e2] = self.ds[e2] +  self.ds[e1]
            for i in self.ds[e1]:
                self.ds[i] = e2


    def Find(self , el):
        if(type(self.ds[el]) == int):
            return self.ds[el]
        return el

    def Finder(self,el):
        if(type(self.ds[el]) == int):
            return self.ds[self.ds[el]]
        return self.ds[el]


n ,q = map(int , raw_input().split())
comm = Size_Set(n)
for _ in xrange(q):
    inp = raw_input().split()
    if(inp[0] == "Q"):
        print len(comm.Finder(int(inp[1])))
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