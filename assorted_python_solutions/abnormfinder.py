a = raw_input("Enter String 1 ")
b = raw_input("Enter String 2 ")
i = 0
while i < len(a):
    if(a[i] != b[i]):
        print "error" , a[i] , " != " , b[i]
        print i/2
    i+=1
