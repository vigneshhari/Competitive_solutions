n , m = map(int , raw_input().split(" "))
lis = map(int , raw_input().split(" "))
mapper = {}
print lis
for i in lis:
    mod = i % m
    print mapper
    if(mod in mapper.keys()):getval = mapper[mod]
    else:getval = []
    if i not in getval:
        getval.append(i)
    mapper[mod] = getval
print mapper