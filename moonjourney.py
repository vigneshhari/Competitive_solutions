N , T = map(int , raw_input().split())
possibledict = []
for i in range(N):
    possibledict.append(set([i]))

def posfinder(lis , data):
    for i,j in enumerate(lis):
        if(data in j):return i
    return -1


for i in range(T):
    A , B = map(int , raw_input().split())
    posa = posfinder(possibledict,A)
    dataa =  possibledict[posa]
    del possibledict[posa]
    posb = posfinder(possibledict,B)
    if(posb == -1):
        possibledict.append(dataa)
        continue
    datab =  possibledict[posb]
    del possibledict[posb]
    possibledict.append(dataa.union(datab))

datafin = [len(i) for i in possibledict]

out = 0
for i in range(0,len(datafin)):
    for p in range(i+1,len(datafin)):
        out += (datafin[i] * datafin[p])

print out






