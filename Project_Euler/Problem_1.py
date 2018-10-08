'''
 Problem 1
 Multiples of 3 and 5
'''
out = 0
for i in range(0,1000):
    if(i % 3 == 0 or i % 5 == 0):
        out += i 
print out
