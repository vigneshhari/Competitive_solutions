
"""
2
3 11
1 2 5
2 7
2 6
"""

minv = []

def backtracker(arr, pos , amount , coins):
    if(amount == 0):
        return coins
    if(pos < 0):return -1
    if(amount < 0):return -1
    times = amount // arr[pos]
    for i in range(times,-1,-1):
        val = backtracker(arr,pos-1 , amount - (i * arr[pos]) , coins+ i )
        if( val != -1):
            return val
    return -1

def dp_solution(coins_avail, amount):
    #coin_used = [ [] for i in range( amount + 1) ]
    dp = [-1 ]* (amount + 1)
    dp[0] = 0
    i = -1
    while i < amount :
        i+=1
        for j in coins_avail:
            if( j > i ):continue
            subsol = dp[ i - j ]
            if( subsol != -1  and  ( dp[i] == -1 or  dp[i] > subsol + 1 )  ):
                dp[i] = subsol + 1
                #coin_used[i] = coin_used[i - j] + [j]
    return dp[amount]



for _ in range(int(input())):
    amount , length = list(map(int , input().split() ))
    coins = list(map(int , input().split() ))
    print(dp_solution(coins , amount))
