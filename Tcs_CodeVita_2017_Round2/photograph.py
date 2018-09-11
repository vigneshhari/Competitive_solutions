
def varience(results):
    # calculate mean
    m = sum(results) / len(results)

    # calculate variance using a list comprehension
    return (sum([(xi - m)**2 for xi in results]) / len(results))


inputs = raw_input().split(",")
data = list(map(int , raw_input().split(",")))
"""data_sort = list(data)
data_sort.sort()
print(data_sort)

print("Printing Varience")
print(data)
print("\n" + str(statistics.stdev(data) )  ) 

sd = statistics.stdev(data)
var = {}
for i in data:
    val = 0
    for k in data:
        if( ((i -k) **2 )< (sd ** 2)  ):continue
        val = val + ((i - k) ** 2)
    var[i] = val
print(var)"""

import itertools 
dictout = {}
temp =  list(itertools.combinations(data,int(inputs[1]),3))
print temp
