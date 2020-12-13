t1, t2, n = map(int , raw_input().strip().split(' '))
ans = [0,t1,t2]

def fibonacciModified(n):
    current = 3
    while current <= n:
        ans.append(ans[current-2] + ans[current-1] ** 2)
        current+=1

fibonacciModified(n)
print ans[n]
