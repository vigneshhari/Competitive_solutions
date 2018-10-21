'''
timing = []
for i in xrange(10000):
    timing.append([])

for i in range(input()):
    start , end , desi = map(int, raw_input().split())
    timing[start].append([desi,0])
    timing[end].append([desi,-1])

sum = 0
current_value = 0
postion_start = -1

for p,i in enumerate(timing):
    if i == [] : continue
    for j in i:
        if(j[1] == 0):
            if(j[0] > current_value):
                max_val = 0
                if(postion_start != -1):
                    for k in range(postion_start , p+1):
                        for l in timing[k]:
                            if(l[1] == 0 and l[0] > max_val):
                                if(l[0] in [_[0] for _ in i ]):
                                    max_val = l[0]
                sum += max_val
                postion_start = p
                current_value = j[0]
                continue
    for j in i:
        if(j[1] == -1):
            if(j[0] == current_value):
                sum += current_value
                current_value = 0
                continue
print sum
'''


# Weighted Job Scheduling

class Star:
    def __init__(self, start, finish, profit):
        self.start  = start
        self.finish = finish
        self.profit  = profit


def bs(star, start_index):
    lo = 0
    hi = start_index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if star[mid].finish < star[start_index].start:
            if star[mid + 1].finish < star[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1

def find(star):
    star = sorted(star, key = lambda j: j.finish)
    n = len(star)
    table = [0 for _ in range(n)]
    table[0] = star[0].profit;
    for i in range(1, n):

        inclProf = star[i].profit
        l = bs(star, i)
        if (l != -1):
            inclProf += table[l];
        table[i] = max(inclProf, table[i - 1])
    return table[n-1]
star = []

for i in range(input()):
    start , end , desi = map(int, raw_input().split())
    star.append(Star(start,end,desi))

print find(star)


# Solved Completely
