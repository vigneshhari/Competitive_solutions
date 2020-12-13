import sys

size , no = map(int , raw_input().split())
array = {}

for i in xrange(no):
    a,b,val = map(int , raw_input().split())
    array[a] = array.get(a,0) + val
    array[b+1] = array.get(b+1,0) - val 

temp = -sys.maxsize -1
val = 0

for i in xrange(size+1):
    val = val + array.get(i,0)
    if(val > temp): temp = val 


print temp 