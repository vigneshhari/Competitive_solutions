
def palindrome(s):
    if (s == s[::-1]):return True
    return False
 
temp = []

for i in range(100,999):
    for k in range(100,999):
        if(palindrome(str(i *k)) == True):
            temp.append(i *k)

print max(temp)