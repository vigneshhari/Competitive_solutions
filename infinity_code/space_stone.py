comp , quer = map(int , raw_input().split(" "))
inps = []
for i in range(0,quer):
    inps.append(map(int , raw_input().split(" ")))

req = []
out = [None] * quer
for j,i in enumerate(inps):
    req.append([i[1],  i[0] , i[0] + i[2] , i[1] ,j]  )

comps_list = []

for i in range(comp):
    comps_list.append(True)

def acquire(num):
    temp = num
    out = 0
    for i in range(comp):
        if(comps_list[i] == True):
            comps_list[i] = False
            out  = out + i + 1
            temp -= 1
        if(temp == 0 ):return out

def release(num):
    temp = num
    for i in range(comp):
        if(comps_list[i] == False):
            comps_list[i] = True
            temp -=1
        if(temp == 0):return

avaliable = comp
ctime = 0
while(True):
    ctime += 1
    for i in range(0,len(req)):
        if(i >= len(req) ):break
        if(req[i][1] >= ctime ):
            if(avaliable >= req[i][0] ):
                out[req[i][4]] =  acquire(req[i][0])
                avaliable -= req[i][0]
                req[i][0] = 0
        if(req[i][2] <= ctime ):
            if(req[i][0] == 0):
                avaliable = avaliable + req[i][3]
                release(req[i][3])
            else:out[req[i][4]] =  -1
            del req[i]
    if(len(req) == 0):break 
            
for i in out:
    print i