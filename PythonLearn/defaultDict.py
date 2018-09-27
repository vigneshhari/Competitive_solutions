from collections import defaultdict

dict = defaultdict(list)

n , m = map(int , raw_input().split())

looper = 1

for i in range(n):
    dict[raw_input()].append(str(looper))
    looper +=1

for i in range(m):
    inp = raw_input()
    if(len(dict[inp]) == 0):
        print -1
    else:
        print (" ".join(dict[inp]))
