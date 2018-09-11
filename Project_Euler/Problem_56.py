
def digitsum(num):
    return sum(map(int , list(str(num)) ))

maxv = 0
for i in range(100):
    for j in range(100):
        maxv = max(maxv , digitsum(i ** j))

print maxv