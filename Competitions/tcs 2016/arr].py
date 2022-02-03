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
print(lis2)