n , q = map(int , raw_input().split())
#class_dict = {1 : [] , 2 : [] , 3 : []}

groups = {}
name_mapper = {}

looper = 0


def countPairs(a, k):
    n = len(a)
    a.sort()
    res = 0
    for i in xrange(n): 
        j = i+1
        while (j < n and a[j] - a[i] < k):
            j += 1
        res += (n - j)
    return res

for i in xrange(1,n+1):
    groups[looper] = [i]
    name_mapper[i] = looper
    looper += 1  


for i in xrange(q):
    data = map(int , raw_input().split())
    if(data[0] == 1):
        one , two = data[1] , data[2]
        pos_one = name_mapper[one]
        pos_two = name_mapper[two]
        if(pos_one == pos_two):continue
        if(len(groups[pos_one]) < len(groups[pos_two]) ):
            groups[pos_two] += groups[pos_one]
            for i in groups[pos_one]:
                name_mapper[i] = pos_two
            del groups[pos_one]
        else:
            groups[pos_one] += groups[pos_two]
            for i in groups[pos_two]:
                name_mapper[i] = pos_one
            del groups[pos_two]
    else:
        c = data[1]
        team_len_list = [len(x) for x in groups.values()]
        print countPairs(team_len_list,c)