def super_reduced_string(s):
    if(len(s) == 0 ):return ""
    out = ""
    prev = s[0]
    looper = 0
    for i in s:
        if(prev == i):
            looper +=1
            if(looper == 2):
                looper = 0
        elif(prev != i):
            if(looper == 1):
                out += prev
            looper = 1
        prev = i

    if(looper == 1):
        out += prev

    return out


s = raw_input()

temper = super_reduced_string(s)

while True:
    temp = super_reduced_string(temper)
    if(temper == temp):break
    temper = temp

if(temp == ""):print "Empty String"
else: print temp