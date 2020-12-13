numq = input()
mains = []
subs = []
for i in  range(numq):
    data = raw_input()
    if(data[0] == "1"):
        num = int(data[1:])
        if(len(mains) != 0):
            if(num >= subs[-1]):
                subs.append(num)
        else:
            subs.append(num)
        mains.append(num)

    elif(data[0] == "2"):
        if(mains[-1] == subs[-1]):
            del subs[-1]
        del mains[-1]
    else:
        print subs[-1]