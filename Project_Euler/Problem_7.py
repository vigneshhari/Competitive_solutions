n = 1
primes = [2]
num = 3
while n < 10001:
    flag = True
    for prime in primes:
        if prime*prime > num:
            break
        if num % prime == 0:
            flag=False
            break
    if flag:
        n+=1
        primes.append(num)
    num += 2
print (primes[-1])
