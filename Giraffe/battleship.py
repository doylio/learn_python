import random


class battleship:
    def __init__(self, n):
        board = [[0] * n for i in range(n)]
        ships = [[1, 5], [2, 4], [3, 3], [4, 3], [5, 2]]
        while len(ships) > 0:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            (dx, dy) = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            clear = True
            for i in range(ships[0][1]):
                if x > n - 1 or y > n - 1 or x < 0 or y < 0:
                    clear = False
                    break
                elif board[x][y] != 0:
                    clear = False
                    break
                x += dx
                y += dy
            if clear:
                ship = ships.pop(0)
                for i in range(ship[1]):
                    x -= dx
                    y -= dy
                    board[x][y] = ship[0]

        self.board = board

    @property
    def isComplete(self):
        for row in self.board:
            if 1 in row or 2 in row or 3 in row or 4 in row or 5 in row:
                return False
        return True

    def fire(self, x, y):
        if self.board[x][y] == 0:
            return 0  # Miss
        else:
            ship = self.board[x][y]
            self.board[x][y] = 0
            for row in self.board:
                if ship in row:
                    return 1  # Hit
            return 2  # Sunk


def random_guessing(game):
    n = len(game.board)
    map = [[-1] * n for i in range(n)]
    turn_counter = 0

    while game.isComplete == False:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        if map[x][y] != -1:
            continue
        result = game.fire(x, y)
        map[x][y] = result
        turn_counter += 1
    return turn_counter


def random_guessing_with_targeting(game):
    n = len(game.board)
    map = [[-1] * n for i in range(n)]
    turn_counter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ship_found = []
    next_moves = []
    direction_found = False

    while game.isComplete == False:
        # check for any ships found
        for ax in range(n):
            for ay in range(n):
                if map[ax, ay] == 1:

        if len(ship_found) > 0:
            move = next_moves.pop(0)
            x = move[0]
            y = move[1]
        else:
            x = random.randint(0, n - 1)
            y = random.randint(0, n - 1)
            if map[x][y] != -1:
                continue
        result = game.fire(x, y)
        map[x][y] = result
        if result == 1:
            ship_found = [x, y]

        if result == 2:

        turn_counter += 1
    return turn_counter

# data = []
# for i in range(1000):
#     game = battleship(10)
#     result = random_guessing(game)
#     data.append(result)
#     print(result)
#
# print('\nSimulation complete!')
# print('Average turn length: ', sum(data) / len(data))