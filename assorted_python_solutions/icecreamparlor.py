from collections import defaultdict

for _ in range(input()):
    flavorDict = defaultdict(list)
    money = input()
    input()
    flavors = map(int , raw_input().split())
    for i in xrange(len(flavors)):
        flavorDict[flavors[i]] = flavorDict[flavors[i]] + [i]
    flag = False
    for i in xrange(len(flavors)):
        for k in  flavorDict[ money - flavors[i]  ] :
            if(i != k ):
                print i+1 , k+1
                flag = True
                break
        if(flag):break
