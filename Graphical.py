import math

import pygame
from Sudoku import run

# Parts of this implementation following Tech with Tim's GUI architecture.

win_Width = 720
win_Height = 720
backdrop_color = [255, 255, 255]  # color of backdrop, currently white
black_line = [0, 0, 0]
grey_line = [200, 200, 200]
board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]



class grid:

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[cube(board[x][y], x, y, width, height) for x in range(0, rows)] for y in range(0, cols)]
        self.current = [0,0]

    def update(self, val, i, j,win):
        self.cubes[i][j].set(val)
        self.draw(win)
        return 1

    def draw(self,win):

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)


    def getBox(self, pos):
        gap = win_Height / 9
        x = math.floor(pos[0]/gap)
        y = math.floor(pos[1]/gap)
        self.current = [x,y]
        return (x,y)

class cube:

    def __init__(self, value, row, col, width, height):
        self.oldValue = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.updateVal = value

    def draw(self, win):
        font = pygame.font.SysFont("Calibri", 30)
        cube_size = self.width / 9
        x = self.col * cube_size
        y = self.row * cube_size
        if self.updateVal == 0:
            # do nothing
            text = font.render(str(self.updateVal), 1, (0,0,0))
        else:
            text = font.render(str(self.updateVal), 1, black_line)
            win.blit(text, (x + cube_size / 2, y + cube_size / 2))


    def set(self, val):
        self.updateVal = val


def displayGridLines(window):
    squares = math.floor(win_Height / 3)
    cells = math.floor(squares / 3)

    for x in range(0, win_Width, cells):
        pygame.draw.line(window, grey_line, (x, 0), (x, win_Height))
    for y in range(0, win_Height, cells):
        pygame.draw.line(window, grey_line, (0, y), (win_Width, y))

    # Thicker lines for each 3x3 square
    for x in range(0, win_Width, squares):
        pygame.draw.line(window, black_line, (x, 0), (x, win_Height))
    for y in range(0, win_Height, squares):
        pygame.draw.line(window, black_line, (0, y), (win_Width, y))

def check(FinishedBoard, cubes):

    for i in range(0,len(cubes)):
        for j in range(0,len(cubes)):
            print("%s %s"%(cubes[j][i
                           ].updateVal,FinishedBoard[i][j]))
            if int(cubes[j][i].updateVal) != int(FinishedBoard[i][j]):
                return 0

    return 1

def Redraw(win,board):
    win.fill((255,255,255))
    displayGridLines(win)
    board.draw(win)

def main():
    pygame.init()
    window = pygame.display.set_mode((win_Width, win_Height))
    window.fill(backdrop_color)
    pygame.display.set_caption("Sudoku Solver")
    displayGridLines(window)
    Board = grid(9, 9, win_Width, win_Height)

    Finished_board = run(board, [], [], 1)
    run2 = True;
    if check(Finished_board, Board.cubes):
        run2 = False;
    while run2:  # main game loop

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run2 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9
                    print(num)
                elif event.key == pygame.K_DELETE:
                    Board.clear()
                elif event.key == pygame.K_RETURN:
                    range = [1,2,3,4,5,6,7,8,9]
                    if num in range:
                        Board.update(num,Board.current[0],Board.current[1],window)
            # update the board to set it as x
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                point = Board.getBox(pos)
                # point[0] is x, point[1] is y
                print(str(point[0]))
                print(str(point[1]))
        pygame.time.delay(1)
        Redraw(window, Board)
        if check(Finished_board, Board.cubes):

            run2 = False;
        pygame.display.update()

main()
pygame.quit()
