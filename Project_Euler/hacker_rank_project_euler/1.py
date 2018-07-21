for _ in range(input()):
    num = input() - 1
    num3 = num //3
    num5 = num //5
    num15 = num//15
    print (( 3 * (num3) * (num3+1) / 2) ) + ( 5 * (num5) *  (num5+1) / 2 ) - ( 15 * (num15) *  (num15+1) /2 )
