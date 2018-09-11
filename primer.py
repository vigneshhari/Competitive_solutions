def answer(n):
    string = "2357"
    num = 10
    while True:
        if (prime(num)): string += str(num)
        if (len(string) >= 10005): break
        num += 1
    ans = 3
    return string[n:n + 5]
import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1  ):
        if (n % i == 0): return False
    return True

print answer(10000)