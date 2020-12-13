#for code monk .. P2 Q1

for i in range(0,input()):
    input()
    dat = list(raw_input().split(" "))
    dat = map(int,dat)
    dat.sort()
    dat.reverse()
    temp = ' '.join(map(str,dat))
    print temp.strip()

