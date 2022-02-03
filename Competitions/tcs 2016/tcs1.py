num = int(input())
temp = [2,3,5,7]
fl = 0
for p in range(9,num,2):
    for it in range(1,len(temp) //2):
        if(temp[it] % p == 0 ):fl = 1;break
    if(fl == 0):temp.append(p)
count = 0
for i in range(len(temp)-1,1,-1):
    sum = 0
    loop = 0
    while sum < temp[i]:
        sum = sum + temp[loop]
        if(sum == temp[i]):count+=1;break
        loop+=1
print(count)