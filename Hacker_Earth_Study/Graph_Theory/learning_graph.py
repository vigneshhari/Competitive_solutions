N,M,K = map(int , raw_input().split(" "))
K= K-1
val = map(int , raw_input().split(" "))

temp = 1

node_val_dict = {}
node_reverse_dict = {}

for i in val :
    node_val_dict[temp] = i
    if(i in node_reverse_dict.keys()):node_reverse_dict[i].append(temp)
    else: node_reverse_dict[i] = [temp]
    temp += 1
nodes = {}

for i in range(1,N+1):
    nodes[i] = []

for i in range(M):
    temp = map(int , raw_input().split(" "))
    nodes[temp[0]].append(temp[1])
    nodes[temp[1]].append(temp[0])

nodes_changed = {}

for i in nodes.keys():
    nodes_changed[i] = [node_val_dict[x] for x in nodes[i]]

ans = []

for i in nodes.keys():
    temp = sorted(nodes_changed[i] , reverse=True)
    if(len(temp)  > K):
        ans.append(temp[K])
    else:ans.append(-1)

tester = 0

for i in ans:
    tester += 1
    if(i == -1):print "-1"
    else:
        if len(node_reverse_dict[i]) > 1:
            temp = sorted(node_reverse_dict[i])
            for x,y in enumerate(temp):
                if(y not in nodes[tester] ):del temp[x]
            print temp
            for j in temp:
                if(j in nodes[tester]):print j;break
        else:
            print node_reverse_dict[i][0]

