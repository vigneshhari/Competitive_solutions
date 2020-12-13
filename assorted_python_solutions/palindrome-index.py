def palindrome_check(string):
    i = 0 
    j = len(string) - 1
    while i <= j:
        if( string[i] != string[j]):return False
        i+=1
        j-=1
    return True


for _ in range(input()):
    inp = raw_input()
    i = 0 
    j = len(inp) -1
    done = True
    while i <= j:
        if(inp[i] != inp[j]):
            if palindrome_check(inp[0:i] + inp[i+1:]):
                done = False
                print i
                break
            elif palindrome_check(inp[0:j] + inp[j+1 : ]):
                done = False
                print j
                break
        i+=1
        j-=1
    if(done):
        print "-1"