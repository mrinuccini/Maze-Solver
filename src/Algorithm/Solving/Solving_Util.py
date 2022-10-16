import tkinter
import numpy as np
import math
from colour import Color

red = Color("red")
colors = list(red.range_to(Color("purple"),400))

# Fait en sorte que tout les murs soit noir et toutes les cellules blanches
def Clear_Maze(maze: np.array, canvas: tkinter.Canvas):
    print(maze.shape)
    for x in range(0, maze.shape[0] - 1):
        for y in range(0, maze.shape[1] - 1):
            if not maze[x][y][3] == 0: continue
            
            color = 'black' if maze[x][y][1] == 1 and maze[x][y][3] == 0 else 'gray' if (50 * x + 38 * y) % 2 == 1 else 'white'
            canvas.itemconfig(maze[x][y][2], fill=color, outline=color)
            
# Returns a table containing the coords of the cell based on the shape of the table
def Get_Cell_Coord(cell_id, shape):
    cell_ratio = cell_id / shape[0]
    cell_coords = ( math.floor(cell_ratio),
                    round((cell_ratio - math.floor(cell_ratio)) * shape[0])
                  )
    return cell_coords

# Returns the eight neighbors of a cell
def Get_Cell_Neighbours(current_cell: tuple, distance: int = 1):
    right = (current_cell[0] + 1, current_cell[1])
    left = (current_cell[0] - 1, current_cell[1])
    top = (current_cell[0], current_cell[1] - 1)
    bottom = (current_cell[0], current_cell[1] + 1)
    
    return [right, left, top, bottom]

def Maze_To_Dict(maze: np.array, use_maze_value: bool = True) -> dict:
    dict_output = {}
    
    for x in range(0, maze.shape[0]):
        for y in range(0, maze.shape[1]):
            dict_output[Get_Cell_Coord(maze[x][y][0], maze.shape)] = maze[x][y] if use_maze_value else [maze[x][y], 0, 0, 0, False, (0, 0), 0]
    
    return dict_output