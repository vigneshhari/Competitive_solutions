import math
circles = []
intersectors = []
ab = input()
a = -1 ;b= -1
for i in range(0,ab):
    circles.append(map(int,raw_input().split(" ")))
for i in circles:
    a+=1
    b=-1
    for k in circles:
        b+=1
        if i == k:continue
        if math.sqrt(((i[0]-k[0]) ** 2) + ((i[1]-k[1]) ** 2)) <= (i[2] + k[2]):
            if([b,a] not in intersectors and (i[0],k[0]) != (i[1],k[1])):
                intersectors.append([a,b])
ans = 0
try:
    while intersectors != []:
        cont = []
        for i in range(0,ab):
            cont.append(0)
        for k in intersectors:
            cont[k[0]] +=1
            cont[k[1]] +=1
        id = cont.index(max(cont))
        len = intersectors.__len__()
        for l in range(0,len):
            if(intersectors[l][0] == id or intersectors[l][1] == id):
                del intersectors[l][0]
                del intersectors[l][0]
        temp = []
        for m in intersectors:
            if(m != []):
                temp.append(m)
        intersectors = m
        ans +=1
except:
    pass
print ans