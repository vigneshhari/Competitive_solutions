a , b = map(int , raw_input().split())

for _ in range(input()):
    low , high = map(int , raw_input().split())
    flag = True
    for i in range(high,low-1,-1):
        if( a % i == 0 and b % i == 0):
            flag = False
            print i
            break
    if(flag):
        print "-1"

# works
