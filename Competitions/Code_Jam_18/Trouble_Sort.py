

times = input()

for __ in range(times):
    input()
    arr = map(int , raw_input().split(" "))
    arr__ = arr[::]
    k = 0 
    while k < len(arr) - 2:
        
        done = True
        i = 0

        while i < len(arr) - 2:
            if ( arr[i] > arr[i+2] ):
                done = False
                arr[i] ,  arr[i+2] = arr[i+2] , arr[i]
            
            i += 1
        if( done == True ):break
        k += 1
    
    done = True

    for i,j in enumerate(sorted(arr__)):
        if( j != arr[i] ):print("Case #{}: {}".format(__+1,i)) ; done = False ;break
    
    if(done == True):
        print("Case #{}: OK".format(__+1))