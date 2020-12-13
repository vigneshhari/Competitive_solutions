input()
data = map(int , raw_input().split())
datadict = {1 : 0 , -1 : 0 , 0 : 0}
for i in data:
    if(i == 0 ):datadict[0]+=1
    elif(i > 0):datadict[1]+=1
    else:datadict[-1]+=1

print '{0:.6f}'.format(datadict[1] * 1.0 / len(data))
print '{0:.6f}'.format(datadict[-1] * 1.0  / len(data))
print '{0:.6f}'.format(datadict[0] * 1.0 / len(data))
