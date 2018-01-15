def space1(i,j):
    out = ""
    for i in range(j-i):
        out +=  " "
    return out

def space2(i):
    out = ""
    for i in range(0,i*2):
        out += " "
    return out

inp = list(raw_input())
inp.reverse()
output = """"""

for i,j in enumerate(inp):
    l = len(inp)
    current = l - i
    if(i == 0):
        output += space1(i,l)
        output += j + "\n"
    else:
        output += space1(i,l)
        output += j
        output += space2(i)
        output += j + "\n"

output = output.rstrip()
print output
reverse_style = output.split("\n")
reverse_style.reverse()
for line in reverse_style:
    print line