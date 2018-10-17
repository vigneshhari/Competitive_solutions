

for _ in range(int(input())):
    length = int(input())
    arr = list(map(int , input().split()))
    dep = list(map(int , input().split()))
    for i in range(length):
        if(arr[i] > dep[i]):
            dep[i] += 2400
    arr.sort()
    dep.sort()
    posarr , posdep ,maxplat = 0,0,0
    platforms = 0
    while posarr < length:
        if(arr[posarr] == dep[posdep]):
            posarr+=1
            posdep+=1
            maxplat = max(maxplat , platforms+1)
        elif(arr[posarr] < dep[posdep]):
            platforms += 1
            posarr +=1
        else:
            platforms -= 1
            posdep +=1
        maxplat = max(maxplat , platforms)
    print(maxplat)
