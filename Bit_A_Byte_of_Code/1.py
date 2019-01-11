n= input()

maxlength = len(str(bin(n))) -2
temp =  "{0:"+str(maxlength)+"d} {0:"+str(maxlength)+"o} {0:"+str(maxlength)+"X} {0:"+str(maxlength)+"b}"
for i in range(1,n+1 ):
    print temp.format(i , i , i , i)
