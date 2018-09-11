
def palindrome(s):
    if (s == s[::-1]):return True
    return False
 
temp = []

for i in range(100,1000):
    for k in range(100,1000):
        if(palindrome(str(i *k)) == True):
            temp.append(i *k)
temp = sorted(temp , reverse = True)

for _ in range(input()):
    inp = input() 
    for i in temp:
        if( i < inp ):
            print i
            break
