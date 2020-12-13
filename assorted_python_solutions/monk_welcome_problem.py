input()
arr1 = map(int , raw_input().split(" "))
arr2 = map(int , raw_input().split(" "))
print " ".join(map(str ,[x + y for x , y in zip(arr1 , arr2) ]))
