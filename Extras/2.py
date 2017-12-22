def low(lis):
    los = len(lis)
    small = 10000000
    ans = 0
    for k in range(1,los+1):
        if(lis[los - k] < small):
            small = lis[los-k]
            ans = los-k
    return ans
try:
    timm = input()
    for i in range(0,timm):
        a = input()
        steps = raw_input().split(" ")
        tot = len(steps)
        steps = map(int,steps)
        current = 0
        ans = 0
        while current + 1 < tot:
            max = steps[current]
            temp = []
            if max == 1:
                temp.append((steps[current] - steps[current+1]) ** 2)
            for k in range(1,max):
                try:
                    temp.append((steps[current] - steps[current + k]) ** 2)
                except:
                    pass
            dat = low(temp)
            ans = ans + temp[dat]
            current = current + 1 + dat
        print ans
except:
    pass


