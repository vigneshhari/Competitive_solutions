N ,Q = map(int , raw_input().split())

lis = [False] * N


for _ in range(Q):
    O , A , B = map(int , raw_input().split())
    if(O):
        temp = 0
        for i in range(A,B+1):
            if(lis[i]):temp+=1    
        print temp 
        continue
    for i in range(A,B+1):
        if(lis[i]):
            lis[i] = not lis[i]
        else:
            lis[i] = not lis[i]

    