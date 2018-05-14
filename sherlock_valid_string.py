inp = raw_input()
ansdict = {}

def tester(dictionary):
    if(len(set(dictionary.values())) == 1):return True
    else:return False

for i in inp:
    ansdict[i] = ansdict.get(i , 0)  + 1

yes = False

if(tester(ansdict)) : yes = True
else:
    for i in ansdict.keys():
        if(ansdict[i] == 1):
            del ansdict[i]
            if(tester(ansdict)):yes = True ; break
            ansdict[i] = 1
        else:
            ansdict[i] = ansdict[i] - 1
            if(tester(ansdict)):yes = True ; break
            ansdict[i] = ansdict[i] + 1

if(yes):print "YES"
else:print "NO"
