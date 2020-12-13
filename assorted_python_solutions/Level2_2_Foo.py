#dont_get_volunteered (Least Knight Moves)

def move(x, y, fx,fy):
    smallest = []
    stack = []
    limit = range(0, 8)
    stack.append((x,y,0))
    movesl = []
    for i in range(0, 8): movesl.append([0] * 8)
    movesl[x][y] = 1
    while len(stack)!= 0:
        new = stack[0]
        x = new[0]
        y = new[1]
        moves = new[2]
        if(x == fx and y == fy):smallest.append(moves)
        moves = moves + 1
        if(x+1 in limit and y+2 in limit and movesl[x+1][y+2] == 0 ):
            stack.append((x+1,y+2,moves))
            movesl[x+1][y+2] = 1
        if(x-1 in limit and y+2 in limit and movesl[x-1][y+2] == 0 ):
            stack.append((x -1, y + 2, moves))
            movesl[x - 1][y + 2] = 1
        if(x+1 in limit and y-2 in limit and movesl[x+1][y-2] == 0 ):
            stack.append((x + 1, y - 2, moves))
            movesl[x + 1][y - 2] = 1
        if(x-1 in limit and y-2 in limit and movesl[x-1][y-2] == 0 ):
            stack.append((x - 1, y - 2, moves))
            movesl[x - 1][y - 2] = 1
        if(x+2 in limit and y+1 in limit and movesl[x+2][y+1] == 0 ):
            stack.append((x + 2, y + 1, moves))
            movesl[x + 2][y + 1] = 1
        if(x+2 in limit and y-1 in limit and movesl[x+2][y-1] == 0 ):
            stack.append((x + 2, y -1, moves))
            movesl[x + 2][y - 1] = 1
        if(x-2 in limit and y+1 in limit and movesl[x-2][y+1] == 0 ):
            stack.append((x -2 , y + 1, moves))
            movesl[x - 2][y + 1] = 1
        if(x-2 in limit and y-1 in limit and movesl[x-2][y-1] == 0 ):
            stack.append((x -2, y -1, moves))
            movesl[x - 2][y - 1] = 1
        del stack[0]
    return min(smallest)





def answer(src, dest):
    if (src == dest): return 0;
    if (src < 0 or dest < 0 or src > 63 or dest > 63): return -1
    x = int(src % 8)
    y = int((src - x) / 8)
    dx = int(dest % 8)
    dy = int((dest - dx) / 8)
    return move(x, y, dx,dy)


for i in range(0,64):
    for k in range(0,64):
        print "For " , i , " " , k , " " ,answer(i,k)


