
import re


def sequence_in(s1, s2):
    """Does `s1` appear in sequence in `s2`?"""
    temp = re.findall(
        "*".join(s1) , s2)
    if(len(temp) >= 1):return True
    return False

maindict = raw_input()
no = input()
for i in range(no):
    ans = 0
    sub = ""
    temp = raw_input()
    for k in range(temp.__len__() - 1 , -1 , -1):
        sub = temp[k] + sub
        if(sequence_in(sub , maindict )):ans +=1
        else:break
    print ans
