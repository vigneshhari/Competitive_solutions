



a,b =0,1
i=1
while True:
    c = a + b
    i+=1
    if(len(str(c)) == 1000):break
    a = b
    b = c

print i