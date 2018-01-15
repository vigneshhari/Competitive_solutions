def check(lis):
    for i in lis:
        if i==0:return False
    return True

a = input()
for k in range(1,a+1):
    mul = 1
    val = input()
    fin = val
    if(val == 0):print "Case #{}: INSOMNIA".format(k);continue
    chk = [0,0,0,0,0,0,0,0,0,0]
    while True:
        for i in str(val):
            chk[int(i)] = chk[int(i)] + 1
        if(check(chk)):
            print "Case #{}: {}".format(k,val)
            break
        mul+=1
        val = fin * mul
        #Case #1: INSOMNIA