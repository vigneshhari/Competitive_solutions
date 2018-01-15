import string
import math

rad = input()
dict = {}
for i in range(26):
    char , val = raw_input().split(" ")
    dict[char.lower()] = float(val)
inp = raw_input().strip()
prev = ''
out = 0
for i in inp:
    i = i.lower()
    if(i not in string.lowercase):continue
    if(i == prev):continue
    if(prev == ''):prev = i ; out += rad ;continue
    temp = abs(( 2 * rad * math.sin(math.radians(abs(dict[prev] - dict[i]) / 2))))
    out = out + temp
    prev = i

print int(math.ceil(out))