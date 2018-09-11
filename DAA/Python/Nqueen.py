print "Enter the Number of Queens / Size of Board"

global SIZE , board
SIZE = input()

board = [ [False] * SIZE   for i in range(SIZE)  ]

def isSafe(row , col):

    for i in range(col):
        if(board[row][i] == True):
            return False
    
    for i,j in zip(range(row,-1,-1) , range(col,-1,-1)):
        if(board[i][j] == True):
            return False

    for i,j in zip(range(row,SIZE,1) , range(col,-1,-1)):
        if(board[i][j] == True):
            return False
    return True


def solveNQueen(col):
    if(col >= SIZE):return True

    for i in range(SIZE):

        if(isSafe(i,col)):
            board[i][col] = True

            if(solveNQueen(col + 1) == True):
                return True
            
            board[i][col] = False
        
    return False

solveNQueen(0)
for i in board:
    print i
        
