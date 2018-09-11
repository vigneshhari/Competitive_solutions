def findcost(floors,base):
    sum = 0
    for i in range(base , base - floors , -1):
        sum = sum + (1000 * (max(1,i) ** 2) ) 
    return sum

time = input()
while time:
    num , base = map(int , raw_input().strip().split(" "))
    buildings = map(int , raw_input().strip().split(" "))
    if(num %2 == 0):
        val = max(buildings[num/2] , buildings[(num/2) -1])
        temp = range((val-num/2)+1 , val+1)
        temp.extend(range( val , val-num/2 ,-1))
    else:
        val = buildings[num/2]
        temp = range((val-num/2) , val)
        temp.extend(range( val , val-num/2 -1 ,-1))
    out = 0
    for i in range(0,num):
        out = out + findcost((temp[i] - buildings[i]) , base) 
    time-=1
    print out