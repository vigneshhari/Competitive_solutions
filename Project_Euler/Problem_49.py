
off = 3330

def normal_prime(num):
    if(num == 1):return 0
    if(num < 3 ):return 1
    if(num % 2 == 0 ):return 0 
    for i in xrange(3,int(num ** 0.5)+1,2):
        if(num % i == 0):return 0
    return 1

def check(val):
    seq = [val , val + off , val + (off * 2)]
    for i in seq:
        if(normal_prime(i) == 0):return False
    if(set(list(str(seq[0]))) == set(list(str(seq[1]))) and set(list(str(seq[1])) )== set(list(str(seq[2])) )):
        return True
    return False        


for i in range(1000,10000):
    if(check(i) == True):
        print i 