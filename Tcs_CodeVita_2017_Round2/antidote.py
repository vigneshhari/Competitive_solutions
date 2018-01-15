size = input()
temp = size
grid = []
while temp:
    grid.append(map(int,raw_input().strip().split(" ")))
    temp-=1
posinf = map(int,raw_input().strip().split(" "))
poscur = map(int,raw_input().strip().split(" "))
posinf[0] = posinf[0]- 1
posinf[1] = posinf[1] -1

poscur[0] = poscur[0]- 1
poscur[1] = poscur[1] -1

infected = [[posinf[0] , posinf[1]]]

infque = []

def infect(posx,posy,level):
    if(level == 2 ):return
    if(posx + 1 < size ):
        if(grid[posx+1][posy] == 1 ):
            if( [posx+1,posy] not in infected ):
                grid[posx+1][posy] = level - 1
                infected.append([posx+1,posy])
                infque.append([posx+1,posy,level-1])
    if(posy + 1 < size):
        if(grid[posx][posy+1] == 1 ):
            if([posx,posy+1] not in infected):
                grid[posx][posy+1] = level - 1
                infected.append([posx,posy+1])
                infque.append([posx,posy +1 ,level-1])
    if(posx + 1 < size and posy + 1 < size):
        if(grid[posx+1][posy+1] == 1 ):
            if([posx+1,posy+1] not in infected):
                grid[posx+1][posy+1] = level - 1
                infected.append([posx+1 , posy+1])
                infque.append([posx+1,posy+1,level-1])
    if(posx + 1 < size and posy - 1 >= 0):
        if(grid[posx+1][posy-1] == 1 ):
            if([posx+1 , posy-1] not in infected):
                grid[posx+1][posy-1] = level - 1
                infected.append([posx+1,posy-1])
                infque.append([posx+1,posy -1,level-1])   
    if(posx - 1 >= 0 ):
        if(grid[posx-1][posy] == 1 ):
            if( [posx-1,posy] not in infected ):
                grid[posx-1][posy] = level - 1
                infected.append([posx-1,posy])
                infque.append([posx-1,posy,level-1])
   
    if(posy - 1 >= 0):
        if(grid[posx][posy-1] == 1 ):
            if([posx,posy-1] not in infected):
                grid[posx][posy-1] = level - 1
                infected.append([posx,posy-1])
                infque.append([posx,posy - 1,level-1])  
    if(posx - 1 >= 0  and posy - 1 >= 0):
        if(grid[posx-1][posy-1] == 1 ):
            if([posx-1,posy-1] not in infected):
                grid[posx-1][posy-1] = level - 1
                infected.append([posx-1 , posy-1])
                infque.append([posx-1,posy -1,level-1])
    if(posx - 1 >= 0 and posy + 1 < size):
        if(grid[posx-1][posy+1] == 1 ):
            if([posx-1 , posy+1] not in infected):
                grid[posx-1][posy+1] = level - 1
                infected.append([posx-1,posy+1])
                infque.append([posx-1,posy+1,level-1])
    if(len(infque) > 0):
        a = infque[0][0]
        b = infque[0][1]
        c = infque[0][2]
        del infque[0]
        infect(a,b,c)
    return

cured = [[poscur[0] , poscur[1]]]
curque = []

def cure(posx,posy,level):
    if(posx + 1 < size ):
        if(grid[posx+1][posy] > 1 ):
            if( [posx+1,posy] not in cured ):
                if(level == 1 ):
                    grid[posx+1][posy] = 1
                else:
                    grid[posx+1][posy] = grid[posx+1][posy] - 1
                cured.append([posx+1,posy])
                curque.append([posx+1,posy,level+1])
    if(posy + 1 < size):
        if(grid[posx][posy+1] > 1 ):
            if([posx,posy+1] not in cured):
                if(level == 1 ):
                    grid[posx][posy+1] = 1
                else:
                    grid[posx][posy+1] = grid[posx][posy+1] - 1
                cured.append([posx,posy+1])
                curque.append([posx,posy +1 ,level+1])
    if(posx + 1 < size and posy + 1 < size):
        if(grid[posx+1][posy+1] > 1 ):
            if([posx+1,posy+1] not in cured):
                if(level == 1 ):
                    grid[posx+1][posy+1] = 1
                else:
                    grid[posx+1][posy+1] = grid[posx+1][posy+1] - 1
                cured.append([posx+1 , posy+1])
                curque.append([posx+1,posy+1,level+1])
    if(posx + 1 < size and posy - 1 >= 0):
        if(grid[posx+1][posy-1] > 1 ):
            if([posx+1 , posy-1] not in cured):
                if(level == 1 ):
                    grid[posx+1][posy-1] = 1
                else:
                    grid[posx+1][posy-1] = grid[posx+1][posy-1] - 1
                cured.append([posx+1,posy-1])
                curque.append([posx+1,posy -1,level+1])   
    if(posx - 1 >= 0 ):
        if(grid[posx-1][posy] > 1 ):
            if( [posx-1,posy] not in cured ):
                if(level == 1 ):
                    grid[posx-1][posy] = 1
                else:
                    grid[posx-1][posy] = grid[posx-1][posy] - 1
                cured.append([posx-1,posy])
                curque.append([posx-1,posy,level+1])
   
    if(posy - 1 >= 0):
        if(grid[posx][posy-1] > 1 ):
            if([posx,posy-1] not in cured):
                if(level == 1 ):
                    grid[posx][posy-1] = 1
                else:
                    grid[posx][posy-1] = grid[posx][posy-1] - 1
                cured.append([posx,posy-1])
                curque.append([posx,posy - 1,level+1])  
    if(posx - 1 >= 0  and posy - 1 >= 0):
        if(grid[posx-1][posy-1] > 1 ):
            if([posx-1,posy-1] not in cured):
                if(level == 1 ):
                    grid[posx-1][posy-1] = 1
                else:
                    grid[posx-1][posy-1] = grid[posx-1][posy-1] - 1
                cured.append([posx-1 , posy-1])
                curque.append([posx-1,posy -1,level+1])
    if(posx - 1 >= 0 and posy + 1 < size):
        if(grid[posx-1][posy+1] > 1 ):
            if([posx-1 , posy+1] not in cured):
                if(level == 1 ):
                    grid[posx-1][posy+1] = 1
                else:
                    grid[posx-1][posy+1] = grid[posx-1][posy+1] - 1
                cured.append([posx-1,posy+1])
                curque.append([posx-1,posy+1,level+1])
    if(len(curque) > 0):
        a = curque[0][0]
        b = curque[0][1]
        c = curque[0][2]
        del curque[0]
        cure(a,b,c)
    return

def prgrid():
    for i in grid:
        for k in i:
            print k,
        print

grid[posinf[0]][posinf[1]] = 5
infect(posinf[0],posinf[1],6)
grid[poscur[0]][poscur[1]] = 1
cure(poscur[0] , poscur[1] , 1)
prgrid()

