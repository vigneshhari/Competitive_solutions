from datetime import  date

temp = 0

for i in range(1901,2001):
    for j in range(1,13):
        if(date(i, j, 1).weekday() == 0 ): temp +=1

print temp