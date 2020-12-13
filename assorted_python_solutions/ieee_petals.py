import math
for i in range(input()):
    val = int(raw_input())
    root = long(math.log(val,2))
    num = long(val) - ((2 ** root))
    if(num < 0 ):num = long(val) - ((2 ** (root-1)))
    print  (2*num)+1



