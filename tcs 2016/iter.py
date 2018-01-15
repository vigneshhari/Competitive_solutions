import copy
temp = []

def manga(lis):
    a = lis[0]/2
    for i in range(0,a):
        lis[0]-=1
        lis[1]+=1
        ab = lis[:]
        temp.append(ab[:])
        ab.append(ab.pop(1))
        print ab
        manga(ab)
    return 0

manga([100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print temp