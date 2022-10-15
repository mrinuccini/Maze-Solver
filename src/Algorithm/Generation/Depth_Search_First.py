from Algorithm.Generation.Algorithm_Util import *
from tkinter.messagebox import showinfo
import random
import time

def Generate_Maze(maze_shape: tuple, editor) -> None:
    # Checks if a generation or a solving is not in progress
    if not editor.sim_data.can_generate:
        showinfo("Warning", "Cannot generate a maze while a generation or a solving is in progress")
        return
    
    editor.sim_data.can_generate = False
    editor.sim_data.can_solve = False
    
    # Create our maze and our grid (the grid store for each cell if it has been visited or not)
    maze = Fill_Maze(maze_shape)
    grid = Fill_Grid(maze_shape)
    
    # Set the cell as visited and break the wall at the location
    current_cell = (1, 1)
    maze[current_cell] = 0
    
    # At the beginning there is only one cell in the stack
    stack = [current_cell]
    nb = 0
    
    while True:
        # If there are no not visited cell anymore, stop the generation
        if len(stack) == 0: break
        
        current_cell = stack.pop()
        grid[current_cell] = 1
        neighbours = []
        list_coord = Get_Neighbours_Cells(current_cell, maze, maze_shape, distance=2)
        
        # Gather all of the neighbor that haven't been visited yet
        for coord in list_coord:
            if Get_Cell(coord, maze_shape, grid) == 0:
                neighbours.append(coord)
        
        # If there are some    
        if len(neighbours) > 0:
            # Remove the wall between the current cell and the neighbor
            current_neighbour = neighbours[random.randint(0, len(neighbours) - 1)]
            wall_between_cell = (int((current_neighbour[0] + current_cell[0]) / 2), int((current_neighbour[1] + current_cell[1]) / 2))
            maze[wall_between_cell] = 0
            maze[current_neighbour] = 0
            
            # Append both the current cell and the neighbor to the stack
            stack.append(current_cell)
            stack.append(current_neighbour)
        else:
            # Else mark this cell as visited
            maze[current_cell] = 499
        
        # Every ten iteration display the maze    
        if nb % 5 == 0:
            Display_Maze(maze, editor, maze_shape)
            
        nb += 1
    
    # Make all the cell that are not wall white
    for coord in maze:
        if not maze[coord] == -1:
            maze[coord] = -2
    
    # Display the maze and redraw the entrance and exit
    Display_Maze(maze, editor, maze_shape)
    Display_Exit_Entrace(editor)
    
    editor.sim_data.can_generate = True
    editor.sim_data.can_solve = True