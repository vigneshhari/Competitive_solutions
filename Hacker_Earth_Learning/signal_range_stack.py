times = input()
while times:
    val = input()
    towers = map(int , raw_input().strip().split(" "))
    temp = 0
    while temp != val:
        current = towers[temp] 
        loopval = 0 ;
        for i in range(0,temp+1):
            if(current > towers[i]):
                loopval+=1
        temp+=1
        print loopval+1,
    print
    times-=1