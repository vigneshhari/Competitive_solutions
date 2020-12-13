b = 28
s = 22
n=int(input())
lis = ['6', str(b)]
a=[]
for i in range(103):
    s += 16
    b += s
    lis.append(b)
for i in range(len(lis)):
    a.append(('0' * (5 - len(str(lis[i]))))+str(lis[i]))
k=0



for i in range(0,n+1):
    if (i!=0):print(' ' * (n - i), end="")
    for j in range(0,i):
        print( a[k], end=" ")
        k+=1
    if(i != 0):print('')
