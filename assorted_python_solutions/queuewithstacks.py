
stack1 = []
stack2 = []

def removetop():
    global stack1 , stack2
    if(stack2 == []):
        while(stack1 != []):stack2.append(stack1.pop())
    stack2.pop()

def printtop():
    global stack1 , stack2
    if(stack2 == []):
        while(stack1 != []):stack2.append(stack1.pop())
    temp = stack2.pop()
    print temp
    stack2.append(temp)

for _ in xrange(input()):
    inp = raw_input().split()
    if(inp[0] == "1"):
        stack1.append(int(inp[1]))
    elif(inp[0] == "2"):
        removetop()
    else:
        printtop()