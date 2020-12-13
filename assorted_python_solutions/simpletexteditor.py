stack = []
string = ""
for i in range(input()):
    inp = raw_input()
    if(inp[0] == "1"):
        string = string + inp[2:]
        stack.append((1,len(inp[2:])))
    elif(inp[0] == "2"):
        stack.append((-1 , string[-1 * int(inp[2:]):]))
        string = string[0:-1 * int(inp[2:])]
    elif(inp[0] == "3"):
        print string[int(inp[2:])-1]
    else:
        if(len(stack) == 0):continue
        data = stack.pop()
        if(data[0] == -1):
            string = string + data[1]
        else:
            string = string[0:-1 * data[1]]
            
        