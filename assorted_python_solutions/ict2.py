import string
low = string.lowercase * 2
up = string.uppercase * 2
out = ""
for i in raw_input():
    if(i in low):
        out = out +  low[low.find(i) + 2]
    elif(i in up ):
        out = out +  up[up.find(i) + 2]
    else:
        out = out + i
print out