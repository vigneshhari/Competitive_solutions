raw_input()

mag = raw_input().split()
need = raw_input().split()

dict = {}
for i in mag: 
    dict[i] = dict.get(i,0) + 1

flag = True

for i in need:
    if(dict.get(i,0) == 0):flag = False
    else:dict[i] -= 1

if(flag):print "Yes"
else:print "No"