# Conway's Game of Life
# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
#    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#    Any live cell with two or three live neighbours lives on to the next generation.
#    Any live cell with more than three live neighbours dies, as if by over-population.
#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
__author__ = "maurizio.boscaini@gmail.com"
__version__ = "1.0, 2016-09-28"

import tkinter
import random
import copy

N_CELLS = 20
ALIVE = 1
DEAD = 0
SEED_CELLS_NUMBER = 60
SIZE = 20

def print_matrix(matrix):
    for row in range(N_CELLS):
        for col in range(N_CELLS):
            print(matrix[row][col], end=" ")
        print()

def draw_matrix(matrix, canvas):
    for row in range(N_CELLS):
        for col in range(N_CELLS):
            if matrix[row][col] == 1:
                canvas.create_rectangle(col*SIZE, row*SIZE, col*SIZE+SIZE, row*SIZE+SIZE, width=1, outline="black", fill='black')
            else:
                canvas.create_rectangle(col*SIZE, row*SIZE, col*SIZE+SIZE, row*SIZE+SIZE, width=1, outline="black", fill='white')
            #print(col*SIZE, row*SIZE, col*SIZE+SIZE, row*SIZE+SIZE)
    
def init_matrix(matrix):
    i = 0

    while i < SEED_CELLS_NUMBER:
        x = random.randint(0, N_CELLS - 1) 
        y = random.randint(0, N_CELLS - 1) 
        if matrix[x][y] == DEAD:
            matrix[x][y] = ALIVE
            i += 1

def count_neighbors(matrix, x, y):
    count = 0
    neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y), (x+1, y),
                (x-1, y+1), (x, y+1), (x+1, y+1)]
    
    for x, y in neighbors:
        if x >= 0 and x < N_CELLS and y >= 0 and y < N_CELLS:
            if matrix[x][y] == ALIVE:
                count += 1
    return count        
    
def transition(matrix):
    # next_matrix = [row[:] for row in matrix] # 1st solution    
    next_matrix = copy.deepcopy(matrix) # 2nd solution
    
    for x in range(N_CELLS):
        for y in range(N_CELLS):
            n_neighbors = count_neighbors(matrix, x, y)
            
            if n_neighbors < 2 or n_neighbors > 3:
                next_matrix[x][y] = DEAD
            elif n_neighbors == 3:
                next_matrix[x][y] = ALIVE
    
    return next_matrix

def update(event=None):
    global matrix
    draw_matrix(matrix, canvas)
    #print_matrix(matrix)
    matrix = transition(matrix)
    top.after(300, update)

matrix = [[0 for x in range(N_CELLS)] for y in range(N_CELLS)]
init_matrix(matrix)
top = tkinter.Tk()
top.geometry(str(N_CELLS*SIZE) +"x"+ str(N_CELLS*SIZE) +"+400+400")
print("250x150+"+ str(N_CELLS*SIZE) +"+"+ str(N_CELLS*SIZE))
canvas = tkinter.Canvas(top)
canvas.pack(fill=tkinter.BOTH, expand=1)
top.after(300, update)
top.mainloop()
