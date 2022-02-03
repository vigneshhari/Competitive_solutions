import time

t1 = time.time()
primes = [2,3,5,7]
for n in range(9,10000,2):
    for x in range(1,(len(primes)//2)):
        if n % primes[x] == 0:
            break
    else:
        primes.append(n)
t2 = time.time()
print(len(primes))
print(t2-t1)