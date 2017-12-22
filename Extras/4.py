T = input()
for i in range(T):
    N = input()
    list = []
    list = map(int, raw_input().split())
    sum = 0
    for index, ele in enumerate(list):
        sum = 0
        i = 0
        for j in range(0, len(list)-index):
            if(index == len(list)-1 or index + i >= len(list) - 1):
                break
            sum += (list[index + j] - list[index]) ** 2
            i += 1
        print sum,