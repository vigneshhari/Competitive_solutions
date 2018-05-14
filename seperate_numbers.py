def solver(start , string , prev = -1):
    if(start >= len(string)):return True
    changer = False
    mover = False
    for i in range(start , len(string)):
        current = string[start:i+1]
        if((int(current) ==  prev +1 and str(int(current)) == current) or prev == -1  ):
            changer = solver(i+1 , string , int(current))
            if(changer == True and prev == -1 ):return current
            mover = True
    if(mover):return changer
    return False

times = input()
for _ in range(times):
    inp = raw_input()
    out =  solver(0 , inp )
    if(out == inp):
        print "NO"
        continue
    print "YES" , out
