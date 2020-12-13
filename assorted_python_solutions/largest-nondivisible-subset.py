_ , N = map(int , raw_input().split())
array = map(int , raw_input().split())

import operator
#s = sorted(s, key = operator.itemgetter(1, 2))

modulos = [ i % N for i in array ]

moduloarray = [[i,0] for i in range(0,N) ]

for i in modulos:
    moduloarray[i][1] += 1

for i,j in enumerate(moduloarray):
    if(j[1] == 0):del moduloarray[i]



moduloarray = sorted(moduloarray, key = operator.itemgetter(1) , reverse = True)

done = []
ans = 0
print moduloarray
for i in moduloarray:
    add = True
    for k in done:
        if(k + i[0] == N and i[1] >= 1):
            add = False
            break
    if(add):
        ans += i[1]
        done.append(i[0])

print ans