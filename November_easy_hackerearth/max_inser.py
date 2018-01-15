
val = input()
uniq = []
current = []
series = [0]
for temp in range(val):
    i , j , k = map(int , raw_input().split(" "))
    if(i in current):series.append(series[0]);series[0] = 0
    current.append(i)
    series[0] += 1
    out = 0
    print series
    for lim in range(j,k+1):
        for t in series:
            if(t >= lim ):out = out + (t//lim)
    print out