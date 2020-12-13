temp = []
check = ["I","E","M"]
current = -1
ongoing = 0
score = 0
i = 0
data = raw_input()
while i < len(data):
    pos = check.index(data[i])
    print score
    if(ongoing == 0):
        if(data[i] != "I"):i=i+1;continue
        else:
            current = 0
            score+=1
            ongoing = 1
    else:
        if(pos == (current + 1)  or pos == current):
            score = score + 1
            current = pos
        else:
            if(current == 2):
                temp.append(score)
                score = 0
                ongoing = 0
                continue
    i=i+1;
if(current ==2):
    temp.append(score)
print temp