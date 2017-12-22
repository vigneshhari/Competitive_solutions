val = input()
for k in range(0,val):
    dat = []
    lav = input()
    for i in range(0,lav):
        dat.append(raw_input())
    max_len = 0
    max = ""
    new = []
    for i in dat:
        p = []
        for l in i:
            if(l not in p):p.append(l)
        new.append("".join(p))
    for i in new:
        if(i.__len__() > max_len):
            max_len = i.__len__()
            max = i
        elif(i.__len__() == max.__len__() and i < max):
            max_len = i.__len__()
            max = i
    print "Case #" +str(k+1) + ": ", dat[new.index(max)]
