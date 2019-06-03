import random

class Tic_Tac_Toe:
    def __init__(self, mode=0):
        self.board = [[0, 0, 0] * 3]
        self.mode = mode

    def play(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = 1
            return 0
        else:
            return -1

    def opponent_move(self):
        if mode == 0:
            return self.random_move()

    def random_move(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while self.board[x][y] == 0:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        self.board[x][y] = -1
        return self.board

    @property
    def is_complete(self):
        #rows
        for row in self.board:
            if abs(sum(row)) == 3:
                return True
        #columns
        for y in range(3):
            col = []
            for row in self.board:
                col.append(row[y])
            if abs(sum(col)) == 3:
                return True
        #Diagonals
        nw = [self.board[0,0], self.board[1,1], self.board[2,2]]
        sw = [self.board[0,2], self.board[1,1], self.board[2,0]]
        if abs(sum(nw)) == 3 or abs(sum(sw)) == 3:
            return True
        return False


class Solver:
    def __init__(self):
        self.states = []
