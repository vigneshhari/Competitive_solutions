import math
"""
count = 0
counter = 0
while True:
    count += 1
    temp = float((( count + 1 ) ** 2) + (4 * ( count ** 2)))
    if((math.sqrt(temp).is_integer() )):
        counter += 1
        print str(counter) , " Number is " , count 
"""

L=15

f1, f2 = 1, 1
for i in range(2*L - 1):
    f1, f2 = f2, f1+f2

print "The", L, "golden nugget =", f1*f2