def pro(n):
    o = 1
    for i in n:
        o *= i
    return o

for _ in range(input()):
    __ , m = map(int , raw_input().split())
    l = map(int , list(raw_input()))
    looper = 0
    maxval = 0
    try:
        while True:
            l[looper + m - 1 ]
            maxval = max( maxval , pro(l[looper : looper + m] ) ) 
            looper +=1
    except:
        pass
    print maxval