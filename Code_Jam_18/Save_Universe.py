
times = int(input())

def findD(seq):
    init = 1
    val = 0
    for i in seq:
        if(i == "C"):init *= 2
        else:val += init
    return val

for k in range(times):
    D , patt = input().split(" ")
    D = int(D)
    patt = list(patt)
    switch,DC,TD = 0,0,0 



    no = 0

    i = len(patt) - 1

    while i >= 0:
        val = findD(patt)
        if(val <= D):break
        if(patt[i] == "S"):
            switch = 1
            i = i - 1 
        elif (switch == 1):
            switch = 0
            no += 1
            patt[i] , patt[i+1] = patt[i+1] , patt[i]
            i = len(patt) -1
        else:
            i = i - 1

        
    if(findD(patt) <= D):print("Case #{}: {}".format(k+1,no))
    else: print("Case #{}: IMPOSSIBLE".format(k+1))
