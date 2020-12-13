inp = input()

"""

# Shittiest Solution Ever **FacePalm**

data= {}
def getgreater(val):
    out = []
    for i in data.keys():
        if(data[i] >= val):out += [i]
    return out

def getsmaller(val,ls):
    out = []
    for i in ls:
        if(data[i] <= val):out += [i]
    return out


def processnode(nodesleft , a):
    orgnodesleft = list(set(nodesleft)  - set([a]))
    nodesleft = orgnodesleft[::]
    #print nodesleft
    if(data[a] == 0):return nodesleft 
    #raw_input()
    for i in getsmaller(data[a],nodesleft):
        nodesleft = orgnodesleft
        if( (data[a] - i) ==  i):continue
        #print data[a] , i , "val is " , ((data[a] - i) in nodesleft) , "second is " , (i in nodesleft)
        if(((data[a] - i) in nodesleft) and (i in nodesleft) ):
            #print "inside with " , data[a] , i
            nodesleft = list(set(nodesleft)  - set([i , data[a] - i ]) )
            #print "new nodes" , nodesleft
            nodesleft = processnode(nodesleft, i)
            nodesleft = processnode(nodesleft , data[a] - i)
            if(nodesleft == []):
                return []
        elif((data[a] - i) == 0):
            nodesleft = list(set(nodesleft)  - set([i]) )
            nodesleft = processnode(nodesleft, i)
            if(nodesleft == []):
                return []
    
    return nodesleft    
"""    


def goodprocessor():
    s1 , s2 = 0,0
    for i in data.keys():
        s1 += i
        s2 += data[i]
    for i in data.keys():
        if(s1 - i == s2):return i

for _ in range(inp):
    SIZE = input()
    data = {}
    for i in range(SIZE):
        a,b = map(int , raw_input().split())
        data[a] = b
    
    print goodprocessor()
    
