n , m , a , b , f , s , t = map(int , raw_input().split())
#class_dict = {1 : [] , 2 : [] , 3 : []}
reverse_class_dict = {}
for i in range(n):
    name , val = raw_input().split()
    val = int(val)
    reverse_class_dict[name] = val

groups = []
name_mapper = {}

looper = 0

for i in reverse_class_dict.keys():
    class_ = reverse_class_dict[i]
    temp = {1 : [] , 2 : [] , 3 : []} 
    temp[class_] = [i]
    groups.append(temp)
    name_mapper[i] = looper
    looper += 1  


for i in range(m):
    one , two = raw_input().split()
    pos_one = name_mapper[one]
    pos_two = name_mapper[two]
    len_one = len(groups[pos_one][1]) +  len(groups[pos_one][2]) + len(groups[pos_one][3]) 
    len_two = len(groups[pos_two][1]) +  len(groups[pos_two][2]) + len(groups[pos_two][3]) 
    if(pos_one == pos_two):continue
    if(len_one + len_two > b ):continue
    if(len(groups[pos_one][1]) + len(groups[pos_two][1]) > f ):continue
    if(len(groups[pos_one][2]) + len(groups[pos_two][2]) > s ):continue
    if(len(groups[pos_one][3]) + len(groups[pos_two][3]) > t ):continue
    groups[pos_one][1] += groups[pos_two][1]
    groups[pos_one][2] += groups[pos_two][2]  
    groups[pos_one][3] += groups[pos_two][3]
    for i in groups[pos_two][1]:
        name_mapper[i] = pos_one
    for i in groups[pos_two][2]:
        name_mapper[i] = pos_one
    for i in groups[pos_two][3]:
        name_mapper[i] = pos_one
     
largest = 0
small_list = []

for i in set(name_mapper.values()):
    small_1 = groups[i][1]
    small_2 = groups[i][2]
    small_3 = groups[i][3]
    lsmall = len(small_1) + len(small_2) + len(small_3)
    if(lsmall < a):continue
    if(lsmall > largest):
        largest = lsmall
        small_list = []
    if(largest == lsmall ):
            small_list = small_list + small_1 + small_2 + small_3
    
if(largest == 0):
    print "no groups"
else:
    for i in sorted(small_list):
        print i
