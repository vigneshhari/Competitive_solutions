from collections import Counter

counter = Counter()
counter_length = Counter()
for i in range(input()):
    query , num = map(int , raw_input().split())
    if(query == 1):
        val = counter.get(num,0)
        if( val == 0 ):
            counter[num] = 1
            counter_length[1] += 1
        else:
            counter_length[val] -=1
            val += 1
            counter[num] = val 
            counter_length[val] += 1
    
    if(query == 2):
        val = counter.get(num,0)
        if(val == 0):continue
        counter[num] -= 1
        counter_length[val] -= 1
        val -= 1
        if(val != 0):
            counter_length[val] +=  1
    
    if(query == 3):
        if(counter_length.get(num,0) > 0):print "1"
        else: print "0"

#Solved