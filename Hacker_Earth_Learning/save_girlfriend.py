# Failed Miserably

val = {}

def find(num):
    init = 0;
    if(num in val.keys()):return val[num]
    for i in range(1,num/2):
        if(num % i == 0):init += 1 
    val[num] = init
    return init

cases = input()
for case in range(cases):
    a,b = map(int , raw_input().split(" "))
    max_floor = []
    for i in range(a,b+1):
        max_floor.append(find(i))
    max_floor.sort()
    temp = max_floor[0]
    life = 1
    for i in max_floor:
        if(i != temp):break
        life += 1
    print life