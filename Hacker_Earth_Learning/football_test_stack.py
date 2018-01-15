times = input()
while times:
    num,top = raw_input().split(" ")
    num = int(num)
    stack = [top]
    while num:
        current = raw_input()
        if(current[0] == "P"):
            stack.append(current[2:])
            before = top
            top = current[2:]
        else:
            stack.append(stack[-2])
        num-=1
    print "Player" , stack.pop()
    times-=1

