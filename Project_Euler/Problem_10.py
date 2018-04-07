

def normal_prime(num):
    if(num == 1):return 0
    if(num < 3 ):return 1
    for i in xrange(3,int(num ** 0.5)+1,2):
        if(num % i == 0):return 0
    return 1

i = 3
out = 2
import time
time1 = time.time()
while i < 2000000:
    if(normal_prime(i)):out+=i  
    i += 2
    
print out , " " , str(time.time() - time1)
