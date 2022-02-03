string = raw_input()
M = 1000000007;

memodict = {}
out = ""
def factorial(num):
    f = 1
    if(num in memodict):return memodict[num]
    for i in range(2,num+1):
        f = (f*i) % M
    memodict[num] = f
    return f
    

for _ in range(input()):
    i , j = map(int , raw_input().split(" "))
    newstring = string[i -1:j ]
    countdict = {}
    evendict = {}
    for i in newstring:
        countdict[i] = countdict.get(i,0) + 1
        if(countdict[i] % 2 == 0):
            evendict[i] = evendict.get(i,0) + 1
    oddno = 0
    for i in countdict.keys():
        if(countdict[i] % 2 != 0):
            oddno += 1
    length = (len(newstring) - max(0,(oddno - 1)))/2
    fact = 1
    for i in evendict.keys() :
        fact = (fact * factorial(evendict[i])) % M
   
    out += str((factorial(length) / fact) * max(1 , oddno) % M) + "\n"

print out 