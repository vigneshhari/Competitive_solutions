def p(n): # will print out primes between 0 and n
  s=[True]*(n/2)
  for i in xrange(int((n/2-1)/2) >> 1):
    for j in xrange((i*(i+3)<<1)+3,n/2,(i<<1)+3): s[j]=False
  return [2] + [((i<<1)+3) for i in xrange(n/2) if (s[i])]

def primechk(val,prime):
    for i in prime:
         for k in prime:
             temp = val -i-k
             if( temp in prime and temp != i and temp != k and i !=k ):
                 print i ,  k , (temp)
                 return 0
    return 0
val = input()
prime = p(val)[2:]
primechk(val,prime)