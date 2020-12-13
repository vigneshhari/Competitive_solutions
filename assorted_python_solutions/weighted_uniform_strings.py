inp_string = raw_input()
storedict = {}
letters = "abcdefghijklmnopqrstuvwxyz"
stringdict = {}
for i,j in enumerate(letters):
    stringdict[j] = i + 1

total = 0
prev = ""
for i in inp_string:
    if(prev != i):
        total = stringdict[i]
    else:
        total = total + stringdict[i]
    storedict[total] = True
    prev = i


inp = input()
for i in range(inp):
    if(storedict.get(input() , False)):
        print "Yes"
    else:
        print "No"
