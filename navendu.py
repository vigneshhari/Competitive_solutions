def answer(x,y):
    if(len(y) > len(x)):x,y = y,x
    for i in x:
        if i not in y:return i
    return -1

print answer([13,5,6,2,5],[5,2,5,13])