import math

def maxPrimeFactors (n):

    for i in range(2,n+1):
        if(n % i == 0):return i

for _ in range(input()):
    gcd_pro = {}
    for i in range(2, input() + 1):
        gcd = i
        current = {}
        while gcd != 1:
            g = maxPrimeFactors(gcd)
            gcd = gcd * 1 / g
            current[g] = current.get(g,0) + 1
        for i in current.keys():
            if(gcd_pro.get(i,0) < current[i] ):
                gcd_pro[i] = current[i]
        
    out = 1 
    for i in gcd_pro.keys():
        out *= (i ** gcd_pro[i]) 
    print out