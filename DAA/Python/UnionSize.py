
class Size_Set:
    def __init__(self,size):
        self.Makeset(size)
    
    def Makeset(self,size):
        self.S = [-1 ] * (size +1)
    
    def Find(self,x):
        if(self.S[x] < 0):
            return x
        else:
            self.S[x] = self.Find(self.S[x]) 
            return self.S[x]
    

    def Union(self,root1,root2):
        f1 = self.Find(root1)
        f2 = self.Find(root2)
        if( self.S[f1] < self.S[f2]):
            self.S[f1] += self.S[f2]
            self.S[f2] = f1
        else:
            self.S[f2] += self.S[f1]
            self.S[f1] = f2
'''
class Size_Set:

    def __init__(self,size):
        self.ds = { i : [i] for i in xrange(size+1) }

    def Union(self,e1 , e2):
        l1  = self.ds[e1]
        l2 = self.ds[e2]
        if(len(l1) > len(l2)):
            self.ds[e1] += self.ds[e2]
            for i in self.ds[e2]:
                self.ds[i] = e1
            self.ds[e2] = e1
        else:
            self.ds[e2] += self.ds[e1]
            for i in self.ds[e1]:
                self.ds[i] = e2
            self.ds[e1] = e2

    def Find(self , el):
        if(type(self.ds[el]) == int):
            el = self.ds[el]
        return len(self.ds[el])
'''