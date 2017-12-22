import math
from decimal import *

def answer(num):
    num = Decimal(num)
    clsqu = num.sqrt()
    if (clsqu - int(clsqu)):
        cei = int(math.pow(int(clsqu) + 1,2))
        flr = int(math.pow(int(clsqu),2))
    else:return int(math.log(num,2))
    step = 0
    stepping = [num - flr ]
    if(num % 2 == 0):
        temp = num / 2
        stepping.append(abs(temp - flr ) + 1)
    else:
        temp1 = (num+1) / 2
        temp2 = (num - 1) / 2
        stepping.append(abs(temp1 - flr) + 2)
        stepping.append(abs(temp2 - flr) + 2)
    step = min(stepping)
    if(cei-num < step):
        step =  cei - num
        flr = cei
    step = int(step + Decimal(flr).log10()/Decimal(2).log10())
    return step

print answer(num)