
for _ in range(input()):

    limit = input()
    a,b = 1,1
    out = 0



    while( True ):
        a,b = b,a + b
        if(b > limit):break
        if(b % 2 == 0):
            out += b
    print out