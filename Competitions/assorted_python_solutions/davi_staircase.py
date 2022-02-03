count = 0
def find_way(n):
    if(n==0):
        global count 
        count +=1
        return 
    if(n < 0):
        return 
    find_way(n-1)  
    find_way(n-2)
    find_way(n-3)

find_way(10)
print count
