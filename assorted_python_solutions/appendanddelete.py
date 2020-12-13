str1 = raw_input()
str2 = raw_input()
times = input()

def getter(st,pos):
    if(pos >= len(st)):return -1
    return st[pos]

posi = 0
for i in range(0,max(len(str1),len(str2))):
    if(getter(str1,i) != getter(str2,i)):break
    posi +=1
moves = ((len(str1) - posi) + len(str2) - posi) 

check = 0

if(moves <= times):
    if(moves != times):
        if(len(str1) + len(str2) < times):
            print "Yes"
            check = 1
        elif((moves - times) %2 != 0):print "No";check = 1
        if(check == 0):print "Yes"
    else:
        print "Yes"
else:print "No"
