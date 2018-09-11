
def moduleu0(num,length,offset):
    while num > length + offset:

        num = num - length
    return num

def minsize(d1,d2,l):
    temp = 0
    while d2 > d1:
        temp = d2
        d2 -= l
    return temp - d1

no = input()


def f(n):
    if (n % 4 == 0):
        return n
    elif (n % 4 == 1):
        return 1
    elif (n % 4 == 2):
        return n + 1
    elif (n % 4 == 3):
        return 0


for i in range(no):
    l,h,n,d1,d2 = map(int , raw_input().split(" "))
    #testing the pos of diagonals
    if(moduleu0(d1,l,n) > (l + n)/2 ):
        newd1 , newd2 = d1,d2
        while d2 > d1 : d2 = d2 - l
        while newd1 < newd2 : newd1 = newd1 + l
        d1,d2 = d2,newd1
    remove = []
    minisize = minsize(d1,d2,l)
    while d1<d2:
        for i in range(d1,d1+minisize+1):
            remove.append(i)
        d1 = d1 + l
    result = 0
    for i in xrange(n , l*h + n):
        if(i in remove):continue
        result ^= i
    print result

