'''
def locate(a, b, c):
    c = c / 2
    r = a - 1
    l = a - 1 - c
    if r == b or l == b:return a
    else:
        if b <= l:return locate(l, b, c)
        else:return locate(r, b, c)

def answer(h, q):
    root = (2 ** h) - 1
    result = []
    for i in range(len(q)):
        if q[i] < root and q[i] >= 1:
            x = locate(root, q[i], root - 1)
            result.append(x)
        else:result.append(-1)
    return result

print answer(5, [19, 14, 28])


from itertools import product 

n , mod = map(int , raw_input().split())
lis = []

def squarer(val):
    return val*val

for _ in range(n):
    get = map(int , raw_input().split())
    lis.append(map(squarer , get[1:]))
maxv = 0
for i in product(*lis):
    if(sum(i) % mod > maxv ):
        maxv = sum(i) % mod
print maxv
'''
'''
missing = -1

def numberlength(number):
    out = 0 
    if(number == 0 ) :return 1 
    while number != 0:
        number = number // 10
        out += 1
    return out  


def checker(number , pos , l):
    temp = 1
    fin = 0
    mover = pos +  numberlength(number) - 1
    while mover >= pos :
        if(mover >= len(l)): return False
        fin = fin +  temp*l[mover]
        temp = temp * 10
        mover -=1
    if(fin == number):return True
    return False

def completed( number , listpos, intstr , chance  ):
    if(listpos  == len(intstr)  ):return True
    correct = checker(number , listpos , intstr)
    if(correct == False and chance == 0):return False
    if(correct == False and chance == 1):
        global missing
        missing = number 
        return completed(number+1 , listpos , intstr , 0)
    return completed(number+1 , numberlength(number) + listpos ,intstr ,  chance )


def getnum(length , l):
    temp = 1
    fin = 0
    mover = length
    while mover >= 0 :
        fin = fin +  temp * l[mover]
        temp = temp * 10
        mover -=1
    return fin

def missingNumber(string):
    l = list(map(int , list(string)))
    done = True
    for i in range(0,(len(string)//2) + 1 ):
        if(completed(getnum(i,l)+1 ,i+1 , l , 1  ) == True):
            return missing
            done = False
            break
    if(done == True):return -1

print(missingNumber("99100101102104"))
'''

'''
def decodeHuff(root, s):
    main_root = root
    i = 0
    while i != len(s):
        root = main_root
        while(s[i] == 1):
            i+=1
            root = root.right
        out += root.left.data
        i += 1
'''