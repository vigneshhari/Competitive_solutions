__author__ = 'vignesh'

str1 = raw_input()
str2 = raw_input()
str3 = raw_input()
str4 = raw_input()
no,lis = (str1.split(" "))
no = int(no)
lis = list(lis) * 3
sum1,sum2 = [],[]
for i in str2.strip():
    sum1.append(i)
for i in str3[1:].strip():
    sum2.append(i)
print sum1,sum2
if(len(sum1) > len(sum2)):sum1,sum2 = sum2,sum1
length = len(sum2)
dat = [0] * length
ans = []
index = 0
while len(sum2) != 0:
    dat1 = 0
    val1,val2 = "",""
    if(len(sum1) != 0 ):
        val1 = sum1[-1]
        dat1 = lis.index(str(val1))
        if(len(sum1) == 1): sum1 = []
        else:del sum1[-1]
    val2 = sum2[-1]
    del sum2[-1]
    dat2 = lis.index(str(val2)) + dat[index]
    sum = dat1 + dat2
    if(sum >= no ):
        diff = (sum) / no
        fsum = sum - (no * diff)
        value = fsum
        if(index +1 != length):
            dat[index+1] =dat[index+1] + diff
        else:
            dat.append(no)
    ans.append(lis[sum])
    index = index + 1
ans.reverse()
print str1
print str2
print str3
print str4
ansprint = " " + ''.join(ans)
print ansprint