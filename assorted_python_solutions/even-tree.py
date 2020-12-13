N ,E = map(int , raw_input().split())
edgedictcount = {}
edgelist = {}
for i in range(1,N+1):
    edgelist[i] = []

for i in range(E):
    U , V = map(int , raw_input().split())
    edgelist[U] = edgelist[U] + [V]
    edgelist[V] = edgelist[V] + [U] 

def nodecounter(cur,pred):
    out = 0
    if(len(edgelist[cur]) == 1) : return 1 
    for i in edgelist[cur]:
        if(i == pred):continue
        out += nodecounter(i,cur)
    edgedictcount[cur] = out + 1
    return out + 1

for i in edgelist[1]:
    nodecounter(i,1)

ans = 0
for i in edgedictcount:
    if(edgedictcount[i] % 2 == 0):ans +=1

print ans