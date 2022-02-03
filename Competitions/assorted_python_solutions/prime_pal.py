'''
def palindrom(n):
    k = 0
    temp = n
    while n > 0:
        k += (n % 10)
        k *= 10
        n = n/10
    return (k/10) == temp
'''

def palindrom(n):
    return list(reversed(str(n))) == list(str(n))
def prime(n):
    for i in range(2,n):
        if(n % i == 0): return False
    return True
i = 0
temp = 2
while i != 100:
    if(palindrom(temp)):
        if(prime(temp)):print temp;i+=1
    temp +=1