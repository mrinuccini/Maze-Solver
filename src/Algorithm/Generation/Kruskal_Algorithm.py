""" Section to allow test modules to use code from source directory """
from lib2to3.pgen2.literals import simple_escapes
import sys
import os
path = os.getcwd()
sys.path.insert(1, f'{path}/src/')
""" End section to allow test modules to use code from source directory """

from GUI.EditorGUI import Editor
from Algorithm.Solving.Dimensions_Code_Algorithm import Get_Cell_Coord
from colour import Color
import random
import time

red = Color("red")
colors = list(red.range_to(Color("violet"),500))

# Create a grid for our maze
def Create_Grid(maze_shape: tuple) -> dict:
    maze = {}
    
    for y in range(0, maze_shape[1]):
        maze[(y, 0)] = -1
    
    for x in range(1, maze_shape[0] - 1):
        for y in range(0, maze_shape[1]):
            if x % 2 == 0:
                maze[(y, x)] = -1
            elif y % 2 == 0:
                maze[(y, x)] = -1
            else:
                maze[(y, x)] = 0
    
    for y in range(0, maze_shape[1]):
        maze[(y, maze_shape[0] - 1)] = -1
       
    nb = 0
     
    for x in range(0, maze_shape[0]):
        for y in range(0, maze_shape[1]):
            if maze[(y, x)] == 0:
                maze[(y, x)] = nb
                nb += 1
    
    return maze

# Use to display the maze to the viewport
def Display_Maze(maze: dict, editor: Editor, shape: tuple) -> None:
    for i in range(0, len(maze)):
        cell_coord = Get_Cell_Coord(i, shape)
        editor.sim_data.cell_list[i].is_wall = True if maze[cell_coord] == -1 else False
        
        if editor.sim_data.cell_list[i].is_wall:
            editor.main_canvas.itemconfig(editor.sim_data.cell_list[i].canvas_object_id, fill='black', outline='black')
        else:
            color = colors[maze[cell_coord] if maze[cell_coord] <= 499 else 499]
            editor.main_canvas.itemconfig(editor.sim_data.cell_list[i].canvas_object_id, fill=color, outline=color)
    editor.update()
    editor.main_canvas.update()

# Checks if the maze is complet
def Is_Finish(maze: dict, maze_shape: tuple) -> bool:
    for x in range(0, maze_shape[0], 2):
        for y in range(0, maze_shape[1], 2):
            if not maze[(y, x)] == maze[(1, 1)]:
                return False
            
    return True

# Generate the maze from the grid
def Generate_Maze(maze: dict, maze_shape: tuple, editor: Editor) -> None:
    nb = 0
    
    while not Is_Finish(maze, maze_shape):
        x = random.randint(1, maze_shape[0] - 2)
        y = 0
       
        if x % 2 == 0:
            y += random.randint(0, int((maze_shape[1] - 1) / 2) - 1) * 2 + 1
        else:
            y += random.randint(0, int((maze_shape[1] - 2) / 2) - 1) * 2 + 2
        
        cell1 = None
        cell2 = None
       
        if maze[(y, x - 1)] == -1:
            cell1 = (y - 1, x)
            cell2 = (y + 1, x)
        else:
            cell1 = (y, x - 1)
            cell2 = (y, x + 1)
        
        if not cell1 == cell2:            
            maze[(y, x)] = maze[cell1]
            
            for x in range(1, maze_shape[0] - 1, 2):
                for y in range(1, maze_shape[1] - 1, 2):
                    if maze[(y, x)] == maze[cell2]:
                        maze[(y, x)] = maze[cell1]
        
        
        Display_Maze(maze, editor, maze_shape)
            
        nb += 1
            
            
            

if __name__ == "__main__":
    editor = Editor()
    maze = Create_Grid((51, 39))
    Display_Maze(maze, editor, (51, 39))
    Generate_Maze(maze, (51, 39), editor)
    while True:
        editor.main_canvas.update()
        editor.update()