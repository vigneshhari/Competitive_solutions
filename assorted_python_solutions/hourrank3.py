n,q,p = map(int , raw_input().split())
glist = map(int , raw_input().split())

def pf(number):
    if(number + p  > n  ) :return 0
    val = glist[number]
    for i in range(number + 1 , number+p):
        val ^= glist[i]
    return val


for i in xrange(q):
    t , a, b = map(int , raw_input().split())
    if( t == 1):
        glist[a-1] ^= b
    else:
        ans = 0
        for i in xrange(a-1,b):
            ans += pf(i)
        print ans