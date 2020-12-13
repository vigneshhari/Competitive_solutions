#for code monk .. P1 Q2pytho


for i in range(0,input()):
    dat = raw_input()
    temp,chk = dat[0],dat[0]
    for i in dat[1:]:
        if chk != i:
            temp = temp + i
        chk = i
    print temp

