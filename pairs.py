n , k = map(int , raw_input().split())
array = sorted(map(int , raw_input().split()) , reverse = True)
counter = 0
for i in range(0,len(array)):
    for j in range(i+1 , len(array)):
        temp = array[i] - array[j]
        if(temp == k):counter+=1;break
        if(temp > k):break
print counter