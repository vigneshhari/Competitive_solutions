
def finder(a,b):
    if(a > b):return 0
    for i in range(2,b):
        if(b % i == 0 ):return 0
    return 1

cases = input()
for case in range(cases):
    inp = input()
    out = 0
    for i in range(1,inp+1):
        for k in range(1,inp+1):
            if(finder(i,k)):out+=1
    print out