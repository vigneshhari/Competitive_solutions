
"""
2
3 11
1 2 5
2 7
2 6
"""

minv = []

def backtracker(arr, pos , amount , coins):
    if(amount == 0):
        return coins
    if(pos < 0):return -1
    if(amount < 0):return -1
    times = amount // arr[pos]
    for i in range(times,-1,-1):
        val = backtracker(arr,pos-1 , amount - (i * arr[pos]) , coins+ i )
        if( val != -1):
            return val
    return -1


for _ in range(int(input())):
    length , amount = list(map(int , input().split() ))
    coins = list(map(int , input().split() ))
    coins.sort()
    minv = []
    print(backtracker(coins , length -1 , amount , 0))
    if(len(minv) == 0):
        print(-1)
    else:print(min(minv))
