def median(l):
    l.sort()

    length = len(l)
    if (length % 2 == 0):
        median = (l[(length)//2] + l[(length)//2-1] + 1.0) / 2
    else:
        median = l[(length-1)//2]

    return median

length , day_l = map(int , raw_input().split())
arr = map(int , raw_input().split())


counter = 0

for i in range(1, length):

    key = arr[i]

    if(i >= day_l):
            if(arr[i] >=  2*median(arr[ i-day_l : i])):
                counter+=1

    j = i-1
    while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
    arr[j+1] = key

print counter
