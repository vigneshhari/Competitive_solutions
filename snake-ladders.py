times = input()
for _ in range(times):   
    Ladders = input()
    ladderdict = {}
    for i in range(Ladders):
        U,V = map(int , raw_input().split())
        ladderdict[U] = V
    Snakes = input()
    snakedict = {}
    for i in range(Snakes):
        U,V = map(int , raw_input().split())
        snakedict[U] = V

    finalmoves = {}

    for i in range(1,100):
        finalmoves[i] = []
        for k in range(1,7):
            move = k + i
            if(move in ladderdict.keys()):move = ladderdict[move]
            if(move in snakedict.keys()):move = snakedict[move]
            finalmoves[i] = finalmoves[i] + [move]

    minmoves = [0] * 100
    ans = 10000000000

    stack = [(1,0)]
    while (stack != []):
        pos , moves = stack[0]
        del stack[0]
        for i in finalmoves[pos]:
            if(i > 99):
                if(moves + 1 < ans):ans = moves + 1
                continue
            if(moves + 1 < minmoves[i] or minmoves[i] == 0  ):
                minmoves[i] = moves + 1
                stack.append((i,moves+1))
    if(ans == 10000000000 ):
        print -1
    else:
        print ans


