MAX_SIZE = 20232;
isPrime = []
SPF = []
prime = []

def mani_sieve(N):
  isPrime[0] = False
  isPrime[1] = False
  for i in range(2,N):
    if( isPrime[i] ):
      prime.append(i)
      SPF[i] = i
    j = 0
    while j< len(prime) and i*prime[j] <N and prime[j] <= SPF[i]:
        isPrime[i*prime[j]] = False
        SPF[i*prime[j]] = prime[j]
        j+=1

def answer(n):
    N= 20232;
    strPrime="";
    for i in range(0,MAX_SIZE):
        isPrime.append(True);
        SPF.append(2);
    mani_sieve(N);
    for i in range(0,len(prime)):
        if prime[i] <=N :
            strPrime+=str(prime[i])
    return strPrime[n:n+5]

print answer(0)
