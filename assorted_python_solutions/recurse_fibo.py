def fibo(n):
    if(n<1):return 0
    if(n==1):return 1
    return fibo(n-1) + fibo(n-2)
print fibo(input())