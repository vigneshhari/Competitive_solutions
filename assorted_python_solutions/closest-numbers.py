input()
numlist = map(int , raw_input().split())
sortedlist = sorted(numlist)
smallestdiff = max(numlist)
out = []
for i in range(0,len(sortedlist) -1):
    diff = abs(sortedlist[i] - sortedlist[i+1])
    if(smallestdiff > diff ):
        smallestdiff = diff
        out = []
    if(smallestdiff == diff):
        out = out + [sortedlist[i] , sortedlist[i+1]]
print " ".join([str(x) for x in out])