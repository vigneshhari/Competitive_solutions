from collections import Counter
data = []
occur = Counter()
for i in range(input()):
    val = raw_input()
    if(occur[val] == 0):
        data.append(val)
        occur[val] +=1
    else:
        occur[val] +=1

ans = [str(occur[i]) for i in data]
print len(ans)
print " ".join(ans)
