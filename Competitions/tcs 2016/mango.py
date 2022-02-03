list = []
list = raw_input().split(" ")
m = int(list[0])
p = int(list[1])

list = [0] * p
count = 0
i = p - 1
while list[i] <= m:
    for j in range(0, m  + 1):
        list[0] = j

        if sum(list) == m:
            count += 1
            print count

    list[1] += 1
    for k in range (1, p -1):
        if list[k] > m:
            list[k+1] += 1
            list[k] = 0
print count