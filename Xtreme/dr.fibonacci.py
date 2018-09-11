
def fib(n):
    a,b,c = 0,1,0
    while c < n:
        a, b , c = b, a + b , c+1
    return b

inp = input()
for i in range(inp):print (fib(input() % 60) % 10)
