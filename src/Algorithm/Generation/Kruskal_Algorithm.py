"""
TODO : Reformat the code (Add a module for futur algorithm)
"""

""" Section to allow test modules to use code from source directory """
import sys
import os
path = os.getcwd()
sys.path.insert(1, f'{path}/src/')
""" End section to allow test modules to use code from source directory """

from Algorithm.Generation.Algorithm_Util import *
import random
from tkinter.messagebox import showinfo
import time

# Create a grid for our maze
def Create_Grid(maze_shape: tuple) -> dict:
    maze = {}
    
    """ Generate the right wall of the maze """
    for y in range(0, maze_shape[1]):
        maze[(y, 0)] = -1
    
    """ Generate the inner grid """
    for x in range(1, maze_shape[0] - 1):
        for y in range(0, maze_shape[1]):
            if x % 2 == 0:
                maze[(y, x)] = -1
            elif y % 2 == 0:
                maze[(y, x)] = -1
            else:
                maze[(y, x)] = 0
    
    """ Generate the left wall for the maze """
    for y in range(0, maze_shape[1]):
        maze[(y, maze_shape[0] - 1)] = -1
    
    """ FIll each cell that is not a wall with a different number """  
    nb = 0
     
    for x in range(0, maze_shape[0]):
        for y in range(0, maze_shape[1]):
            if maze[(y, x)] == 0:
                nb += 1
                maze[(y, x)] = nb
    
    """ Returns the maze """
    return maze

# Checks if the maze is complet
def Is_Finish(maze: dict, maze_shape: tuple) -> bool:
    """ Checks if every cell contain the same number """
    for x in range(1, maze_shape[0], 2):
        for y in range(1, maze_shape[1], 2):
            if not maze[(y, x)] == maze[(1, 1)]:
                return False
            
    return True

# Generate the maze from the grid
def Generate_Maze(maze_shape: tuple, editor) -> None:
    # Checks if a generation or a solving is not in progress
    if not editor.sim_data.can_generate:
        showinfo("Warning", "Cannot generate a maze while a generation or a solving is in progress")
        return
    
    editor.sim_data.can_generate = False
    editor.sim_data.can_solve = False
    
    # Create the maze
    maze = Create_Grid(maze_shape)
    
    
    Display_Maze(maze, editor, maze_shape)
    nb = 0
    
    # While the maze is not generated
    while not Is_Finish(maze, maze_shape):
        """ Pick a random wall """
        x = random.randint(1, maze_shape[0] - 2)
        y = 0
       
        if x % 2 == 0:
            y += random.randint(0, int((maze_shape[1] - 1) / 2) - 1) * 2 + 1
        else:
            y += random.randint(0, int((maze_shape[1] - 2) / 2) - 1) * 2 + 2
        
        cell1 = None
        cell2 = None
       
        """ Get the two cell around the wall """
        if maze[(y, x - 1)] == -1:
            cell1 = maze[(y - 1, x)]
            cell2 = maze[(y + 1, x)]
        else:
            cell1 = maze[(y, x - 1)]
            cell2 = maze[(y, x + 1)]
        
        """ If the cells don't contain the same number """
        if not cell1 == cell2:            
            maze[(y, x)] = cell1
            
            """ Fill all the cell that contains number b with number a """
            for y_ in range(1, maze_shape[1] - 1):
                for x_ in range(1, maze_shape[0] - 1):
                    if maze[(y_, x_)] == -1: continue

                    if maze[(y_, x_)] == cell2:
                        maze[(y_, x_)] = cell1

        """ Every 20 iterations : display the maze """
        if nb % 20 == 0:               
            Display_Maze(maze, editor, maze_shape)
            
        nb += 1
    
    """ make all the cell in the maze white """
    for key in maze:
        if not maze[key] == -1:
            maze[key] = -2
    
    """ Make the maze complex by breaking a few random walls """     
    for x in range(0, maze_shape[0]):
        x = random.randint(0, (maze_shape[0] - 3)) + 1
        y = 0
        
        if x % 2 == 0:
            y += random.randint(0, int((maze_shape[1] - 1) / 2) - 1) * 2 + 1
        else:
            y += random.randint(0, int((maze_shape[1] - 2) / 2) - 1) * 2 + 2
        
        maze[(y, x)] = -2
        Display_Maze(maze, editor, maze_shape)
            
    # Display the maze one more time
    Display_Maze(maze, editor, maze_shape)
    
    # Redraw the exit and entrance
    editor.main_canvas.itemconfig(editor.sim_data.entrance_cell.canvas_object_id, fill="blue", outline="blue")
    editor.main_canvas.itemconfig(editor.sim_data.exit_cell.canvas_object_id, fill="green", outline="green")
    
    editor.sim_data.can_generate = True
    editor.sim_data.can_solve = True