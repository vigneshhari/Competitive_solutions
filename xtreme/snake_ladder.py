def pos(i,j,maxv):
    if(j %2 == 1 ):
        return (maxv *(j-1)) + i
    else:
        return  (maxv * (j-1) ) + ( maxv +1 - i)

def getposition(n,maxv):
    j = (n//maxv) +1
    if(j%2 == 1):
        i= (n % maxv ) + 1
    else:
        i = (maxv) - (n % maxv)
    return i,j


size  = input()
players = input()
currentstate = [0 ] * players
snakes = {}
for snake in xrange(input()):
    startx , starty , endx , endy = map(int , raw_input().split())
    snakes[ pos(startx,starty,size)   ] = pos(endx , endy,size)
ladders = {}
for ladder in xrange(input()):
    startx , starty , endx , endy = map(int , raw_input().split())
    ladders[ pos(startx,starty,size)   ] =    pos(endx , endy,size)


for i in snakes.keys():
    stackframela = []
    stackframesn = []
    current = snakes[i]
    stackframesn.append(i)
    while( ladders.get(current,-2) != -2 or snakes.get(current,-2) != -2 ):
         if(ladders.get(current,-2) != -2 ):
             stackframela.append(current)
             current = ladders[current]
         elif(snakes.get(current,-2) != -2):
             stackframesn.append(current)
             current = snakes[current]
    for j in stackframela:
        ladders[j] = current
    for j in stackframesn:
        snakes[j] = current


for i in ladders.keys():
    stackframela = []
    stackframesn = []
    current = ladders[i]
    stackframela.append(i)
    while( ladders.get(current,-2) != -2 or snakes.get(current,-2) != -2 ):
         if(ladders.get(current,-2) != -2 ):
             stackframela.append(current)
             current = ladders[current]
         elif(snakes.get(current,-2) != -2):
             stackframesn.append(current)
             current = snakes[current]
    for j in stackframela:
        ladders[j] = current
    for j in stackframesn:
        snakes[j] = current

current_player = 0

won = 0

for dieroll in xrange(input()):
    if(won == players):
        raw_input()
    if(currentstate[current_player] <= size * size ):
        die1 , die2 = map(int , raw_input().split())

        die = die1 + die2
        current = currentstate[current_player]+ die

        if(ladders.get(current,-2) != -2 ):
            current = ladders[current]
        elif(snakes.get(current,-2) != -2):
            current = snakes[current]

        currentstate[current_player] = current
        if current > (size * size) : won+=1


    current_player+=1
    if(current_player == players):
        current_player = 0

for j,i in enumerate(currentstate) :
    if(i > size * size):
        print "{} winner".format(j + 1)
    else:
        if(i == 0):
            x,y = 0,1
        else:
            x, y = getposition(i-1,size)
        print "{} {} {}".format(j+1 , x ,y)


# Problem Completely Solved
