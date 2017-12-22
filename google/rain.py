import copy

val = input()
for m in range(0,val):
    dat = raw_input().split(" ")
    wat = []
    for i in range(0,int(dat[0])):
            wat.append(raw_input().split(" "))
    small = 1001
    for i in range(1,int(dat[1]) -1):
        if(int(wat[0][i]) < small ):small = int(wat[0][i])
    for i in range(1,int(dat[1]) -1):
        if(int(wat[-1][i]) < small ):small = int(wat[-1][i])
    for i in range(1,int(dat[0]) -1):
        if(int(wat[i][0]) < small):small = int(wat[i][0])
        if(int(wat[i][-1]) < small):small = int(wat[i][-1])
    water = 0

    for i in range(1,int(dat[0]) - 1):
        for k in range(1,int(dat[1]) - 1):
            if int(wat[i][k]) < small:
                water = water + small - int(wat[i][k])
    print "Case #" +str(m+1) + ": ", water,small