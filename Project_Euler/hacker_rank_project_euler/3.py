
for _ in range(input()):
    val = input()
    i = int(val**.5)


    def normal_prime(num):
        if(num == 1):return 0
        if(num <= 3 ):return 1
        if(num % 2 == 0 ):return 0 
        for i in xrange(3,int(num ** 0.5)+1,2):
            if(num % i == 0):return 0
        return 1
    printed = 1
    while (i > 0):
        if(val % i == 0):
            if(normal_prime(i) == 1):
                print i
                printed = 0
                break
        i -= 1
    if(printed):print val