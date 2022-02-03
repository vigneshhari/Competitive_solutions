length , tries = map(int , raw_input().split())
ans = 0
for _ in range(tries):
    code , out = map(int , raw_input().split())
    ans += (length - out)
print ans

#Incomplete
