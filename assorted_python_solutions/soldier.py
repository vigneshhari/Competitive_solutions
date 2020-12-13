__author__ = 'vignesh'

import math

def distance(a,b,c,d):
    dist = math.sqrt((a-c)**2 + (b-d)**2)
    return dist

no = input()
shelter,soldier = [],[]
for i in range(no):
    shelter.append([float(x) for x in raw_input().split(" ")])
for i in range(no):
    soldier.append([float(x) for x in raw_input().split(" ")])
totaldis = 0
dis = []

for i in soldier:
    lis = [distance(i[0],i[1],x[0],x[1]) for x in shelter]
    dis.append(min(lis))
    del shelter[lis.index(min(lis))]
print max(dis)
print sum(dis)