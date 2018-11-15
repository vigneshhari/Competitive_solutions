


def dpsolver(coins , amount ):
    coin_hist = [0] * (amount +1)
    coin_hist[0] = 1
    for i in coins:
         for j in range(0,amount+1):
             if( j < i ):continue
             coin_hist[j] += coin_hist[j - i]
    print(coin_hist)

dpsolver([1,2,5] , 12)
