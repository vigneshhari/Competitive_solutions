import copy
import string
lower = string.lowercase * 2
password = list(raw_input())
current = copy.deepcopy(password)
for i in xrange(input()):
    values = raw_input().split(" ")
    values = [int(x)-1 for x in values]
    if(values[0] == 0):
        if(current[values[1]:values[2]+1] == current[values[3]:values[3]+(values[2] - values[1] + 1) ]):
            print "Y"
        else:
            print "N"
    if(values[0] == 1):
        current[values[1]:values[2] +1] = current[values[3]:values[3]+(values[2] - values[1] + 1) ]
    if(values[0] == 2):
        current[values[1]:values[2] +1] = [lower[lower.index(x) + 1] for x in current[values[1]:values[2] +1]]
