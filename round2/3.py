
dat = map(int,raw_input().split())
lf=[]
rgb = ['R','G','B']
for m in range(0,dat[0]):
    lf.append(map(str,raw_input().split()))
for l in range(0,dat[1]):
    ques = raw_input().split()
    ini = [[] * dat[0]]
    freq = ques[0]
    for i in range(0,dat[0]):
        ini.append([])
        for k in range(0,dat[0]):
            val = lf[i][k]
            ans = int(freq) / int(val)
            finans = rgb[ans % 3]
            ini[i].append(finans)
    del ini[-1]
    value =0
    val = [int(ques[1]) -1 , int(ques[2]) -1 , int(ques[3]) -1 , int(ques[4]) -1]
    for i in range(0,dat[0]):
        for k in range(0,dat[0]):
            if(i >= val[0] and k >= val[1] and k <= val[3] and i <= val[2] and str(ini[i][k]) == str(ques[-1]) ):
                value+=1
    print value
