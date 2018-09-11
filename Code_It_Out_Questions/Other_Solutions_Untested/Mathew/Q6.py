
table = []
calculated = []

def solve( i,  make):
    if(make<0): return 0
    if(make==0): return 1
    if(i>numCoins): return 0
    if(calculated[i][make] == False): #eliminating overlap
        table[i][make] = solve(i, make - c[i]) + solve(i+1, make)
        calculated[i][make] = True
    return table[i][make]
c = []
make, numCoins = map(int, input().strip().split())
for i in range(1,numCoins+1):
    c.append(int(input()))
print(solve(1, make))
