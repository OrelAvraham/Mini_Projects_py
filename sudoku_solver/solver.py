import time

"""
Some things you should know when using this code:
    1. All the functions uses the global board
    2. 0 in the board represents an empty slot

Sudoku board examples:

Solved board:
[[8, 2, 7, 1, 5, 4, 3, 9, 6],
         [9, 6, 5, 3, 2, 7, 1, 4, 8],
         [3, 4, 1, 6, 8, 9, 7, 5, 2],
         [5, 9, 3, 4, 6, 8, 2, 7, 1],
         [4, 7, 2, 5, 1, 3, 6, 8, 9],
         [6, 1, 8, 9, 7, 2, 4, 3, 5],
         [7, 8, 6, 2, 3, 5, 9, 1, 4],
         [1, 5, 4, 7, 9, 6, 8, 2, 3],
         [2, 3, 9, 8, 4, 1, 5, 6, 7]]

Not Solved board:
[[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

Shape of the board:
[[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []]
"""

board = [[0, 0, 7, 2, 0, 0, 9, 0, 0],
         [0, 0, 0, 0, 9, 4, 0, 0, 0],
         [6, 0, 9, 0, 0, 0, 7, 0, 8],
         [0, 3, 0, 8, 0, 7, 0, 0, 6],
         [0, 8, 0, 0, 0, 0, 0, 4, 0],
         [5, 0, 0, 4, 0, 3, 0, 9, 0],
         [1, 0, 6, 0, 0, 0, 2, 0, 9],
         [0, 0, 0, 9, 6, 0, 0, 0, 0],
         [0, 0, 3, 0, 0, 2, 4, 0, 0]]


def print_board():
    global board

    for i, y in enumerate(board):
        if i in [3, 6]:
            print('------+-------+------')

        for j, x in enumerate(y):
            if j in [3, 6]:
                print('|', end=' ')
            print(x, end=' ')
        print()
    print()


def possible(y, x, n):
    global board

    # check the row
    for i in range(0, 9):
        if board[y][i] == n:
            return False

    # check the column
    for i in range(0, 9):
        if board[i][x] == n:
            return False

    # find the starting x,y of the square you are in
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    # check the square
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0 + i][x0 + j] == n:
                return False

    # if we haven't found n in the row, the column and the square you can put n here
    return True


def solve():
    global board

    # go over all y and x
    for y in range(9):
        for x in range(9):
            # if slot is empty try to fill it with al the options until one works
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0

                return

    print_board()
    input('Press Enter for More Solutions')


print_board()
t0 = time.time()
solve()
print(time.time()-t0)