def count(n,div):
    out = 0
    for i in range(1,n+1):
        if(i % div == 0):continue
        if(n% i == 0):out += 1
    return out

no , a , b = map(int,raw_input().split())

for i in range(no):
    pd = input()
    final = 0
    for k in range(a,b+1):
        final += count(k,pd)
    print final
