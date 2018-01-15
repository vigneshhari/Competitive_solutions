def pather(pos):
    paths = 0
    if pos == [1,1]: return 1
    if pos[0] <= const[0] and pos[1] >= const[1]: return 0
    if pos[0] > 1:
        paths += pather([pos[0]-1,pos[1]])
    if pos[1] > 1:
        paths += pather([pos[0],pos[1]-1])
    return paths

test = input()
for i in range(0,test):
    lis = map(int,raw_input().split(" "))
    gridSize = [lis[0],lis[1]]
    const = [lis[2],lis[3]]
    result = pather(gridSize)
    print result
