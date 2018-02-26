limit = 4000000
a,b = 1,1
out = 0



while( a < limit ):
    a,b = b,a + b
    if(a % 2 == 0):
        #print a 
        out += a
print out