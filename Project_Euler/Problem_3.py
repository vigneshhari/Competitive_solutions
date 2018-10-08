n = 600851475143
i=2
while i*i < n:
    if n % i == 0:
        while n%i == 0:
            n//=i
    i+=1
if n%i == 0:
    print(i)
else:
    print(n)
