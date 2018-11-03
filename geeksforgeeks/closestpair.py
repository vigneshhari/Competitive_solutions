
#Python2



'''
Sample input

1,4,5,7
10,20,30,40
32

1,4,5,7
10,20,30,40
50

'''

arr1 = map(int , raw_input().split(",") )
arr2 = map(int , raw_input().split(",") )
x = input()


difference = abs(arr1[0] + arr2[0] -x)
pos1 = 0
pos2 = 0

temper = 0

while True:
    if(pos1 == len(arr1) -1 or  pos2 == len(arr2) - 1  or temper == len(arr1) + len(arr2) ):
        break
    if( difference > abs(arr1[pos1 + 1] + arr2[pos2] - x) or difference > abs(arr1[pos1 ] + arr2[pos2 + 1 ] - x )  ):
        change1 = abs(arr1[pos1 + 1] + arr2[pos2] - x)
        change2 = abs(arr1[pos1] +  arr2[pos2 + 1] - x)
        if(change1 > change2):
            pos2+=1
        else:
            pos1+=1
        difference = abs(arr1[pos1] + arr2[pos2] -x)

    temper +=1

while pos1 != len(arr1) - 1:
    if(  difference < abs(arr1[pos1 + 1] + arr2[pos2] - x)):
        break
    pos1 +=1
    difference = abs(arr1[pos1] + arr2[pos2] -x)

while pos2 != len(arr2) - 1:
    if(  difference < abs(arr1[pos1 ] + arr2[pos2 +1] - x)):
        break
    pos2 +=1
    difference = abs(arr1[pos1] + arr2[pos2] -x)


print arr1[pos1] , arr2[pos2]



#Complete
