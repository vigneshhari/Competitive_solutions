'''
 Problem 48
 Self powers
'''
sumv = 0
for i in range(1 , 1001):
    sumv += (i ** i)
print str(sumv)[-10:]
