from collections import Counter

input()

data = Counter(map(int , raw_input().split()))

ans = 0

for i in range(input()):
    size , amount = map(int , raw_input().split())
    if(data[size] != 0):
        data[size] -= 1
        ans += amount


print ans
