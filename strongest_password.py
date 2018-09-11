numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

input()
inp = raw_input()
pdict = {}
n , l , u , s = 1,1,1,1
for i in inp:
    if(n == 1):
        if(i in numbers):n = 0
    if(l == 1):
        if(i in lower_case):l = 0
    if(u == 1):
        if(i in upper_case):u = 0
    if(s == 1):
        if(i in special_characters):s = 0

final = n + l + u + s
needlength = 6 - len(inp) 
print max(final , needlength)