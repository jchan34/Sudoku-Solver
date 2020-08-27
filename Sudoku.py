import math

# Parts of implementation following Tech with Tim's algorithm.
# March 15, 2020

board1 = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 7]];

board2 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]

prev_col = []
prev_row = []


# returns 1 if illegal, 0 if legal number
def illegalCheck(num, row, col, board):
    for i in range(len(board[row])):
        if board[row][i] == num and i != col:
            return 1;
    for j in range(len(board)):
        if board[j][col] == num and j != row:
            return 1;

    x_min = math.floor(row / 3);
    y_min = math.floor(col / 3);
    for x in range(x_min * 3, x_min * 3 + 3):
        for y in range(y_min * 3, y_min * 3 + 3):
            if board[x][y] == num and x != row and y != col:
                return 1;

    return 0;


# finds empty position to start, returns -1 if no more empty pos on board
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
            elif i == len(board) - 1 and j == len(board[i]) - 1:
                return -1, -1


# prints board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -");
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="");

            if j != 8:
                print(str(board[i][j]) + " ", end="");
            else:
                print(str(board[i][j]));


# Solves the board
def run(board, prev_row, prev_col, num):
    i, j = findEmpty(board)
    finished = False
    if i and j == -1:
        print("Sudoku Finished!")
    else:
        for num in range(num, 10):
            check = illegalCheck(num, i, j, board)
            if check == 0:
                board[i][j] = num;
                printBoard(board);
                prev_row.append(i)
                prev_col.append(j)
                num = 0
                break
            elif num == 9:
                num = (board[prev_row[len(prev_row) - 1]][prev_col[len(prev_col) - 1]])
                board[prev_row[len(prev_row) - 1]][prev_col[len(prev_col) - 1]] = 0;
                prev_col.pop(len(prev_col) - 1)
                prev_row.pop(len(prev_row) - 1)

        run(board, prev_row, prev_col, num + 1);

    return board

# Run!
board = run(board2, prev_row, prev_col, 1)
