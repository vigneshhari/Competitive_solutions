
def max_funny(inp , pos ):
    stack = []
    cur = inp[pos]
    length = 1
    for i in range(pos+1 , len(inp)):
        length += 1
        if(inp[i] == cur):print inp[pos:i+1] ; stack.append(length)
    print stack
    return max(stack)

input()
inp = raw_input().split(" ")
looked= []
large = 0
for j,i in enumerate(inp):
    if i not in looked:
        new = max_funny(inp[:] , j )
        looked.append(i)
        if(new > large):large = new
print new