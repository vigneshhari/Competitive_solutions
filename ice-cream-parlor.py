inp = input()
for _ in range(inp):
    M = input()
    input()
    data = map(int , raw_input().split())
    done = False
    for i in range(0,len(data)):
        if(done):break
        checker = M - data[i]
        for j in range(i+1 , len(data)):
            if(data[j] == checker):
                print i +1, j+1
                done = True
                break