inp = input()

def checker(strval , curpos , pointer , avail):
    if(strval == ""):return True
    check = True
    if(pointer == -1):
        for i,j in enumerate(avail):
            if(j[0] == strval[curpos]):
                if(checker(strval , curpos +1 , i , avail) == True):check = False  
    else:
        if(curpos == len(avail[pointer])):
            del avail[pointer]
        
        if(avail[pointer] == strval[curpos + 1]):
            return checker(strval,curpos+1,pointer , avail)
    if(check):return False
    return True
        

for _ in xrange(inp):
    input()
    passvals = raw_input().split()
    checker(raw_input() , 0 , -1 , passvals  )
    