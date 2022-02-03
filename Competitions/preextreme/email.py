email = raw_input()
length = len(email)

def checkdot(string,position):
    for i in range(position,len(string)-2):
        if(string[i:i+3] == "dot"):
            return True
    return False

i = 0
ans = ""
while i < length:
    if( i + 2 < length and i != length - 3  ):
        if(i != 0 and email[i:i+3] == "dot"):
            ans += "."
            i+=3
            continue
    if(i + 1 < length and i != 0 and i != length - 2):
        if( email[i:i+2] == "at"  ):
            if(checkdot(email,i)):
                ans += "@"
                i = i+2
                continue

    ans += email[i]
    i+=1
print ans


#Incomplete
