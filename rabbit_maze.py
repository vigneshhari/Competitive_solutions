class mazeb:
    xlim = 0
    ylim = 0
    min_moves = []
    board = [[]]
    def maze_solver(self,x,y,moves,moved_pos):
        if(x not in range(0,self.xlim+1) or y not in range(0,self.ylim+1)):return
        if(len(self.min_moves) > 0):
            if(moves > min(self.min_moves)):return
        if(x == self.xlim and y == self.ylim):self.min_moves.append(moves);return
        if((x,y) in moved_pos):return
        else: moved_pos.append((x,y))
        if(y -1 >= 0):
            if(self.board[y-1][x] == 0):
                self.maze_solver(x,y-1,moves+1,moved_pos[:])
        if(y +1 <= self.ylim):
            if(self.board[y+1][x] == 0):
                self.maze_solver(x,y+1,moves+1,moved_pos[:])
        if (x + 1 <= self.xlim):
            if (self.board[y][x + 1] == 0):
                self.maze_solver(x+1 , y , moves + 1,moved_pos[:])
        if (x - 1 >= 0):
            if (self.board[y][x - 1] == 0):
                self.maze_solver(x - 1, y , moves + 1, moved_pos[:])
        return




def answer(maze):
    test = mazeb()
    test.board = maze
    test.xlim = len(test.board[0]) - 1
    test.ylim = len(test.board) - 1
    if(test.xlim not in range (2,21) or test.ylim not in range(2,21)):return -1
    test.maze_solver(0, 0, 1, [])
    for i in range(0,test.ylim+1):
        for k in range(0,test.xlim+1):
            if(test.board[i][k] == 1):
                test.board[i][k] = 0
                test.maze_solver(0, 0, 1, [])
                test.board[i][k] = 1
    return min(test.min_moves)



print answer(  [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])