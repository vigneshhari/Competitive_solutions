def finder(lis , pos,value):
    for i,j in enumerate(lis):
        if(j[pos] == value):
            return i
    return  -1

def finder2(lis , pos,value,pos2,value2):
    for i,j in enumerate(lis):
        if(j[pos] == value and j[pos2] == value2):
            return i
    return  -1

for i in range(input()):
    tweight ,no = map(int , raw_input().split(" "))
    lis = []
    for k in range(no):
        a,b = map(int , raw_input().split(" "))
        lis.append((b/(a*1.0) , a , b))
    tp = 0
    ans = 0
    while tweight > 0 :
        if(no == 0):break
        try:
            pos = finder(lis , 0 ,(max(map(lambda x: x[0], lis))))
            val = lis[pos][0]
        except:
            break

        if len([x for x in lis if x[0] == val ]) > 1:
            test =  [x[2] for x in lis if x[0] == val ]
            maxval = max(test)
            pos = finder2(lis , 0 , val , 2 , maxval)
        val = lis[pos]
        if(lis[pos][1] <= tweight  ):
            tweight = tweight - lis[pos][1]
            ans += lis[pos][2]
            no -= 1
        del lis[pos]

    print ans