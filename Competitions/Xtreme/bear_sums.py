for _ in range(input()):
    q , length = map(int, raw_input().split())
    lis = map(int, raw_input().split())
    inv = {}
    for i in lis:
        inv[i] = 0
    flag = True
    done = False
    for i in range(length-1):
        if(sum(lis[i:i+2]) == q):
            print "ans" ,min(lis[i:i+2]) , max(lis[i:i+2])
            done = True
            flag = False
            break
    for i in lis
        for j  in lis:
            flag=flag
    for i in lis:
        if(done == True):break
        if( inv.get(q - i , -1) != -1   ):
            if(q-i == i and  lis.count(i) == 1  ):continue
            print "ans " , min(i , q-i) , max(i , q-i)
            flag = False
            break
    if(flag):
        print "!OK"


# Partially Solved
