def reverse(a):
    return([a[1],a[0]])

test = input()
for i in range(0,test):
    ovr = input()
    runs = map(int,raw_input().split())
    pat = [0,1]
    play = [0,0,0,0,0,0,0,0,0]
    balls_f = 0
    overs = 0
    for i in runs:
        if(balls_f == 6):
            overs+=1
            balls_f = 0
            pat = reverse(pat)
        if(overs == ovr):break
        if(i == -1):
            a = max(pat) + 1
            pat[0] = a
            if(a==11):break
        if(i != -1):
            play[pat[0]] = play[pat[0]] + i
        if(i == 3 or i == 1):pat = reverse(pat)
        balls_f +=1
    play = map(str,play)
    print " ".join(play)

