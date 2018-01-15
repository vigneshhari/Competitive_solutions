def fin(num,lis):
    lens = lis.__len__()
    for i in range(1,lens+1):
        if(lis[lens-i] <= num):return lens-i
    print lis , "    " , min(lis)
    return lis.index(min(lis))
input()
lis = raw_input().split(" ")
len = len(lis)
for i in range(0,len):
    lis[i] = int(lis[i])
lis = sorted(lis)
ans = 0
for k in range(1,len+1):
    num = k ** 2
    ret = fin(num,lis)
    print num - int(lis[ret])
    if(num - int(lis[ret]) > 0):
        ans = ans + num - int(lis[ret])
    '''else:
        ans = ans + (num - int(lis[ret])) * -1
    '''
    del lis[ret]
print ans
