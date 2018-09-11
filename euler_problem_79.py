sub_list = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
sub_list = map(str , sub_list)

#Creating Objects

dict_connec = {}
for i in range(0,10):dict_connec[str(i)] = []

#Removing Non Existent Objects

dict_connec.__delitem__("5")
dict_connec.__delitem__("4")

# making connections

for i in sub_list:
    for j in range(0,2):
        dict_connec[i[j]].append(i[j+1])


# For Removing Duplicates

for i in dict_connec.keys():
    dict_connec[i] = list(set(dict_connec[i]))

def find_weight(num):
    temp = 0
    for i in dict_connec[num]:
        temp += len(dict_connec[i])
    return max(temp,0,len(dict_connec[num]))

ans = ""

# Taking most connected ones

DISCOURSE = [5,4]

print dict_connec

for i in range(0,10) :
    if(i in DISCOURSE ):continue
    print i , " Has Connections " , find_weight(str(i))