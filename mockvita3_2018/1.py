def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b 
    return sum(digits[::-1])

def insertionSort(arr):
 
    moves = 0

    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        while j >=0 and key < arr[j] :
                moves +=1
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return moves


input()

data = [ numberToBase(x,6) for x in  map( int , raw_input().split(",") )] 

print insertionSort(data)

