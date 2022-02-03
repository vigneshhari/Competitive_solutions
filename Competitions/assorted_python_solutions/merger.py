#for code monk .. P2 Q3

for i in range(0,input()):
    raw_input()
    arr1 = [int(x) for x in raw_input().split(" ")]
    arr2 = [int(x) for x in raw_input().split(" ")]
    arr1.append(-1)
    arr2.append(-1)
    a1,a2 = 0,0
    while True:
        if(arr1[a1] == -1 and arr2[a2] == -1):break
        if(arr1[a1] > arr2[a2]):
            print arr1[a1],
            a1 = a1+1
        else:
            print arr2[a2],
            a2 = a2+1
    print ""
