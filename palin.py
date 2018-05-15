
inp = input()
for _ in range(int(inp)):

    cv = raw_input()
    val = list(map( int , cv))
    cv= int(cv)
    if(cv < 10):
        if(cv == 9):print(cv + 2)
        else :print(cv+1) ; continue
    for i in range(1,20):
        if(cv  == int("9" * i )):
            print(cv + 2)
            cv = -1
    if(cv == -1):continue

    llen = len(val)
    middlef , middlel = 0,0
    if(llen % 2 == 0):
        middlel =  llen // 2
        middlef = middlel - 1
    else:
        middlel = llen // 2
        middlef = middlel

    startindex = 0
    lsmall = False
    same = True
    while startindex < llen/2:

        if(val[startindex] == val[(startindex + 1) * -1] and same == True ):
            same = True
        else:
            same = False
        if(val[startindex] < val[(startindex + 1) * -1]):
            lsmall = True
            val[(startindex + 1) * -1] = val[startindex]
        elif(val[startindex] > val[(startindex + 1) * -1]):
            val[(startindex + 1) * -1] = val[startindex]
            lsmall = False

        startindex += 1
    
    if(lsmall or same):
        val[middlef] = val[middlef] + 1
        val[middlel] = val[middlef]
        while(val[middlef] == 10):
            val[middlef] = 0
            val[middlel] = 0
            middlef -= 1
            middlel += 1
            val[middlef] = val[middlef] + 1
            val[middlel] = val[middlel] + 1


    print("".join(map(str , val)))
