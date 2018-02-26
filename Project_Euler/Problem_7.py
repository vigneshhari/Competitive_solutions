import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1  ):
        if (n % i == 0): return False
    return True

num = 10001
i = 2
ans = 0
while (num != 0):
    if(prime(i) == True):
        ans = i
        num -= 1
    i += 1
print ans
    