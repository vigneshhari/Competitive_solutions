b_d = { "{" : "}" , "(" : ")" , "[" : "]"}
for i in range(input()):
    stack = ["$"]
    done = 1
    for k in raw_input():
        if(k in ["{" , "[" , "("]):
            stack.append(b_d[k])
        else:
            if(stack[-1] != k ):
                done =0 
                break
            else:
                stack.pop()
    if(len(stack) != 1):done = 0
    if(done):print "YES"
    else: print "NO"