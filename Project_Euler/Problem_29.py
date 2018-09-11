vals = []

for i in range(2,101):
    for j in range(2,101):
        vals.append(i ** j)

print len(set(vals))