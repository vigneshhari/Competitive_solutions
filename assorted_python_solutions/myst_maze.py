__author__ = 'vignesh'
import copy

rc = input()
maze = []
for i in range(rc-1):
    maze.append( ["X"] * (rc))
maze.append(["-"] * rc)

def mazer(x,y):
    if(x == rc- 1):
        maze[x][y] = "O"
    else:
        maze[x][y] = "-"
    try:
        if(maze[x][y+1] == "X"  and maze[x][y-1] == "X"  and maze[x-1][y] == "X" and  maze[x+1][y] == "X"):return False
    except:
        pass
    for i in range(0,rc):
        if(maze[0][i] == "-" ):
            if(search(copy.deepcopy(maze),0,i)):
                return True
    return False

def search(mazed,x, y):
    if mazed[x][y] == "O":
        return True
    elif mazed[x][y] == "X" or mazed[x][y] == "V":
        return False
    mazed[x][y] = "V"

    if ((x < len(mazed)-1 and search(mazed,x+1, y))
        or (y > 0 and search(mazed,x, y-1))
        or (x > 0 and search(mazed,x-1, y))
        or (y < len(mazed)-1 and search(mazed,x, y+1))):
        return True
    return False

looper = 0
check = True
while True:
    looper+=1
    temp = raw_input()
    if(temp == "-1"):break
    xv,yv = (int(x) for x in temp.split(" "))
    if(mazer(xv - 1,yv -1)):
        print looper;check=False;break
if(check):print -1

