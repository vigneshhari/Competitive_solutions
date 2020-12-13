for i in range(input()):
    stra = raw_input()
    strb = raw_input()
    dict = {}
    for i in stra:
        dict[i] = True
    flag = False
    for i in strb:
        if (dict.get(i,False)):
            flag = True
            break
    if(flag):print "YES"
    else:print "NO"

# Solved