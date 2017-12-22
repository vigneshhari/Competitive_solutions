baa = input().split(" ")
a = [int(baa[0]),int(baa[1])]

lis11 = input().split(" ")
lis22 = input().split(" ")
lis1 = []
lis2 = []
for i in range(0,len(lis11)):
    at = int(lis11[i])
    bt = int(lis22[i])
    lis1.append(at)
    lis2.append(bt)
temp = 0
i = 1
index = 0

print(lis2)

big = lis2[0]
if lis2[0] < 0:
    big = lis2[0] * -1

while i < a[0]:
    if lis2[i] < 0:
        temp = lis2[i] * -1
    else:
        temp = lis2[i]
    if temp > big:
        big = temp
        index = i
    i += 1
if lis2[index] < 0:
    lis1[index] += a[1] * 2
else:
    lis1[index] -= a[1] * 2
i = 0
sum = 0
while i < a[0]:
    sum += lis1[i] * lis2[i]
    i+=1
print (sum)