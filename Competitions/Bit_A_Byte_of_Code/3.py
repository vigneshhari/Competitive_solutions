
n = input()
data = raw_input().split()
counter = 0
c = input()
"""
def backtracker(len,count):
    global counter
    print len , counter , count
    if(count == 0):return
    if(data[len] == "a"):
        counter += max(n - len - 1 , count)
        return
    if(len == n-1 ):return
    for i in range(len , n ):
        backtracker(i , count -1)


for k in range(n):
    backtracker(k , c -1 )


print counter

"""

from itertools import combinations

comb = combinations(data, c)
le= 0.0
for i in list(comb):
    le+=1
    print i
    if "a" in i:
        counter +=1

print counter/le
