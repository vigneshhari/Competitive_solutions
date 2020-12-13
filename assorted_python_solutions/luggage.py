#for code monk .. P2 Q2

for i in range(0,input()):
    friends = input()
    friend_weight = []
    for friend in xrange(0,friends):
        friend_weight.append(input())
    out = []
    for k in range(0,friends):
        temp = 0
        for day in friend_weight[k:]:
            if(day < friend_weight[k]):
                temp = temp +1
        out.append(temp)
    print ' '.join([str(x) for x in out])