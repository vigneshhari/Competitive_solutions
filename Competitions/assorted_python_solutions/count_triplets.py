size , cr = map(int , raw_input().split() )

pos_mapper = {}


data = map(int , raw_input().split())

for i,j in enumerate(data):
    if(pos_mapper.has_key(j)):
        pos_mapper[j] += [i]
    else:
        pos_mapper[j] = [i]

counter = 0

for j,i in enumerate(data):
    if( pos_mapper.has_key(i * cr) and pos_mapper.has_key(i * cr * cr)  ):
        for pos_1 in pos_mapper[i*cr]:
            if( pos_1 > j):
                for pos_2 in pos_mapper[i*cr*cr]:
                    if(pos_2 > pos_1 > j):counter+=1

print counter

# Incomplete