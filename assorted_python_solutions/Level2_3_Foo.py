def prod(n):
    out = 1
    for i in n:out *= i
    return out

def answer(list):
    if(len(list) > 50):return "-1"
    if(len(list) == 1):return str(list[0])
    list.sort()
    neg = [];pos=[]
    for i in list:
        if i < 0 : neg.append(i)
        elif(i>0):pos.append(i)
    if(len(neg) % 2 != 0):del neg[-1]
    if(len(pos) == 0):return 0
    return str(prod(pos) * prod(neg))

print answer( [-2,-3,-4,-5])