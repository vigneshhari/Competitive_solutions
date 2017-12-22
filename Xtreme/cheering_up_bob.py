moves = {}
for i in range(1,10):
    moves[i] = map(int , raw_input().split(" "))

board = ['-'] * 10

def CheckWin():
    if(board[0] == board[1] and board[1] == board[2] and board[0] == 'X'):
        return [0,1,2]
    elif(board[3] == board[4] and board[4] == board[5] and board[3] == 'X'):
        return [3, 4, 5]
    elif(board[6] == board[7] and board[7] == board[8] and board[6] == 'X'):
        return [6, 7, 8]
    elif(board[0] == board[3] and board[3] == board[6] and board[0] == 'X'):
        return [0, 3, 6]
    elif(board[1] == board[4] and board[4] == board[7] and board[1] == 'X'):
        return [1, 4, 7]
    elif(board[2] == board[5] and board[5] == board[8] and board[2] == 'X'):
        return [2, 5, 8]
    elif(board[0] == board[4] and board[4] == board[8] and board[4] == 'X'):
        return [0, 4, 8]
    elif(board[2] == board[4] and board[4] == board[6] and board[4] == 'X'):
        return [2, 4, 6]
    return False

def dicttonum(lis):
    return ((lis[0] - 1) * 3) + (lis[1] -1)

for i in range(1,10):
    print dicttonum(moves[i])
    board[dicttonum(moves[i])] = "X"
    winningpos = CheckWin()
    print board
    if CheckWin() != False:print i ; break

print winningpos