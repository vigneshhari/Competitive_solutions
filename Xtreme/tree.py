import math


def findlca(a,b):
    while True:
        if(a == b):
            return a
        if(a > b):
            a = a//2
        else:
            b = b//2



inp = input()
for i in range(inp):
    a,b = map(int ,raw_input().split(" "))
    lca = findlca(a,b)
    print int(math.log(a,2)) + int(math.log(b,2)) - (2 * int(math.log(max(lca,1),2) ))

