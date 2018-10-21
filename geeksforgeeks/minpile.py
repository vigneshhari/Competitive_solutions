"""
3
4 0
2 2 2 2
6 3
1 2 5 1 1 1
6 3
1 5 1 2 5 1
"""


def findreqcoins(arr):
    minel = min(arr)
    reqcoins = 0
    for i in arr:
        if(i > minel and i - minel - lim > 0):
            reqcoins += i - minel - lim
    return (reqcoins)
'''
for _ in range(int(input())):
    length , lim = list(map(int , input().split() ))
    arr = list(map(int , input().split() ))
    values = [findreqcoins(arr)]
    for i in range(length):
        values.append(findreqcoins(arr[0:i] + arr[i+1:]) + arr[i])
    print(min(values))
'''

for _ in range(int(input())):
    length , lim = list(map(int , input().split() ))
    arr = list(map(int , input().split() ))
    arr.sort()
    for i in range()
    print(arr)


# Incomplete
