'''

The Sieve Method to Find if a number is prime or not

'''

all_num = {} #This dict will store all final results i.e which all numbers are prime or not

def sieve_check(num):
    for i in xrange(2,int(num ** 0.5)):
        if(all_num.get(i,0) == 0):
            for k in xrange(2,num):
                if(i*k  > num):break
                all_num[i*k] = 1
                if(num % k == 0):return


def normal_prime(num):
    if(num < 3 ):return 1
    if(num % 2 == 0 ):return 0 
    for i in xrange(3,int(num ** 0.5)+1,2):
        if(num % i == 0):return 0
    return 1

for i in range(input()):
    if(normal_prime(input()) == 1):
        print "prime"
    else:
        print "composite"
#print sieve_check(3659707955798852)