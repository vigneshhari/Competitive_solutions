times = input()
data = []
for i in range(times): 
    data.append(input())
for s in sorted(data, key=int):
    print(s)