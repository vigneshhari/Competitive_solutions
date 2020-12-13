size = input()
students = set(map(int , raw_input().split(" ")))
range_set = set(range(1,size+1))
s = ""
for i in sorted(list(range_set - students)):    
    s = s + str(i) + " "
print s[:-1]