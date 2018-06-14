length , k = map(int , raw_input().split())
data = map(int , list(raw_input()))
i = 0
abnor = []
while(i < length/2 ):
    if(data[i] != data[-1 * (i+1)]):
        abnor.append(i)
    if(data[i] > data[-1 * (i+1)]):
        data[-1 * (i+1)] = data[i]
        k-=1
    elif(data[i] < data[-1 * (i+1)]):
        data[i] = data[-1 * (i+1)]
        k-=1
    i=i+1
if(k >= 0 ):
    i = 0
    while(i < length/2 and k > 0 ):
        if(i in abnor and data[i] != 9):
            if(k > 0):
                data[i] = 9
                data[-1 * (i+1)] = 9
                k -= 1
        elif(data[i] != 9):
            if(k > 1):
                data[i] = 9
                data[-1 * (i+1)] = 9
                k -= 2
        i+=1
    if( k > 0):
        if(length % 2 != 0):
            data[length/2] = 9
    print "".join(map(str , data))
elif(k<0):
    print "-1"
