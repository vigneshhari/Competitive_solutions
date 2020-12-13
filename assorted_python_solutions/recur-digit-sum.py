def sumfinder(num):
    return sum(map(int , list(str(num))))

N ,T = map(int , raw_input().split())
N = (sumfinder(N) * T)
temp = 0
while(True):
    temp = sumfinder(N)
    if(temp == N):break
    N = temp

print temp


