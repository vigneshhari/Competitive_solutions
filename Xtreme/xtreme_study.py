dictionary = {}

temp = []

while True:
    val = raw_input()
    if(val == ""):break
    splitted = val.split(" ")
    temp.append((int(splitted[0]) , splitted[1:]))

temper = []

for i in temp:
    for k in i[1]:
        if(k not in temper):temper.append(k)
    if(len(i[1]) not in dictionary.keys() ):dictionary[len(i[1])] = []
    dictionary[len(i[1])].append(i)

for i in dictionary.keys():
    dictionary[i] = sorted(dictionary[i], key=lambda t: t[0])

low = []

need = temper.__len__()

def lowest(n,have,time):
    if(len(have) == need):return
    for i in dictionary[n]:
        if(list(set(temper) - set(have)) in i[1]):return 
    for i in range(len(have),need):
