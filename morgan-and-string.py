_ = input()
for __ in range(_):
    val1 = raw_input().upper()
    val2 = raw_input().upper()
    loop1 , loop2 = 0,0
    out = ""
    while loop1 != len(val1) or loop2 != len(val2):

        if(loop1 != len(val1) and loop2 != len(val2) ):
            if(val1[loop1] < val2[loop2]):
                out = out + val1[loop1]
                loop1 +=1
            elif(val1[loop1] > val2[loop2]):
                out = out + val2[loop2]
                loop2 +=1
        
        mover = False
        if(loop1 != len(val1) and loop2 == len(val2)):
            out = out + val1[loop1 : ]
            print "stuff of 1" ,val1[loop1 :]
            mover = True
        if(loop1 == len(val1) and loop2 != len(val2)):
            out = out + val2[loop2 : ]
            print "stuff of 2 " , val2[loop2 :]
            mover = True
        if(mover):break
        temp1 = loop1
        temp2 = loop2

        while(val1[temp1] == val2[temp2]):
            temp1 +=1
            temp2 +=1
            if(temp1 == len(val2)):
                out = out + val1[loop1]
                loop1 +=1
                break
            elif(temp2 == len(val2)):
                out = out  + val2[loop2]
                loop2+=1
                break
            if(val1[temp1] < val2[temp2]):
                print "here bef " , out
                out = out + val1[loop1 : temp1]
                loop1 = temp1
                print "here her " , out 
                break
            elif(val1[temp1] > val2[temp2]):
                out = out + val2[loop2 : temp2]
                loop2 = temp2
                break

    
    print out


"""
6
DAD
DAD
ABCBA
BCBA
BAC
BAB
DAD
DABC
YZYYZYZYY
ZYYZYZYY
ABCDA
ABCDB

1
ABCDA
ABCDB

"""
