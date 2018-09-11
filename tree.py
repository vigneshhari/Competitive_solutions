

num = 28

level = 5

temp = (2 ** (level-1))-1
sub = 0
if num > temp:
    num = num - temp ;
    sub = 1

ans = 0

import math

count_main = 0;
for i in range(level-2 , -1 , -1):
    count_2 = 0.0
    for k in range(1,2**i +1):
        count_main+=1
        count_2 +=1
        if(count_main == num):
            ans =  count_main + math.ceil(count_2/2) + ((2**i) - k)
            break
if(ans > temp):ans = (2 ** (level))-1
if(sub == 1): ans = ans + temp

print int(ans)