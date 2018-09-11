
ans = [0] * 1000001

def normal_prime(num):
    if(num == 1):return 0
    if(num <= 3 ):return 1
    if(num % 2 == 0 ):return 0 
    for i in xrange(3,int(num ** 0.5)+1,2):
        if(num % i == 0):return 0
    return 1
primes = []

sum_v = 0
looper = 2
while looper < 1000001:
    if(normal_prime(looper)):
        sum_v += looper
    ans[looper] = sum_v
    looper +=1

for _ in range(input()):
    print ans[input()]
    