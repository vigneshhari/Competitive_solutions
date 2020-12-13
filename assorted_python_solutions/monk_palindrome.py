n = input()
while n:
    val = raw_input()
    leng = len(val) - 1
    temp =  "".join([ val[leng-x]  for x,y in enumerate(val) ])
    # to reverse temp = val[::-1]
    if( val == temp):
        if(leng % 2 == 0):
            print "YES ODD"
        else:
            print "YES EVEN"
    else:
        print "NO"
    n-=1

