

array = [-1] * 65
array[0] = 0

for i in range(1,65):
    ans = 1
    for j in range(i):
        ans += array[j]
    array[i] = ans

for _ in range(int(input())):
    print(array[int(input())])
