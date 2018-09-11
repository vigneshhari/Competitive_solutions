for _ in range(input()):
    val = input()
    n = ( ((val * (val+1)) /2 ) ** 2)
    n2 =  ( (val * (val+1) * ((2 * val) + 1)    ) /6 ) 
    print abs(n-n2)