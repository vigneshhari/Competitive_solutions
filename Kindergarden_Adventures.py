n = input()
lis = map(int , raw_input().split())
arr = [0] * (n)
for j,i in enumerate(lis):
    if(i >= n ):continue
    if(i == 0):continue
    #print arr , j +1 , j - i + 1
    arr[(j+1) % n] += 1
    arr[j-i + 1 ] -= 1
maxv = -999999999999999
maxp = 0
temp = 0
for j,i in enumerate(arr):
    temp = temp + i
    if(temp > maxv):
        maxv = temp
        maxp = j
print maxp + 1
'''
6
1 5 4 3 6 8
'''