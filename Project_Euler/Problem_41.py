#create all pandigital numbers
def normal_prime(num):
    if(num % 2 == 0 ):return 0 
    for i in xrange(3,int(num ** 0.5)+1,2):
        if(num % i == 0):return 0
    return 1
maxval = 0
def pancheck( mov_lis , current_val  ):
    if(len(mov_lis) == 0):
        print current_val
        if(normal_prime(current_val) == 1):
            global maxval
            maxval = max(maxval , current_val)
        
    for i in mov_lis:
        pancheck(mov_lis - set([i]) , (current_val * 10) + i )

for i in range(2,11):

    lis = set(range(1,i))
    pancheck(lis , 0)

print "The Maximum of all Pandital Prime is " , str(maxval)