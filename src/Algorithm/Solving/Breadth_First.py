from GUI.Simulation_Data import Simulation_Data
from Algorithm.Solving.Solving_Util import *
from tkinter.messagebox import showinfo
import numpy as np

def Solve(sim_data: Simulation_Data, editor, maze: np.array):
    # Checks if a solving or a generation is not in progress
    if not editor.sim_data.can_solve: 
        showinfo("Warning", "Cannot solve the maze while a generation or a solving is in progress")
        return
    
    editor.sim_data.can_generate = False
    editor.sim_data.can_solve = False
    
    Clear_Maze(maze, editor.main_canvas)
    
    print("Solving Maze...")
    dict_output = Maze_To_Dict(maze)

    entrance_cell_coords = Get_Cell_Coord(sim_data.entrance_cell.cell_id, maze.shape)
    exit_cell_coords = Get_Cell_Coord(sim_data.exit_cell.cell_id, maze.shape)
    direction_to_process = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    coords_to_process = [exit_cell_coords]
    next_process = []
    processed_coords = []
    is_searching = True

    while is_searching:
        for coord in coords_to_process:
            for direction in direction_to_process:
                current_tile = (coord[0] + direction[0], coord[1] + direction[1])

                # If it is out of bounds
                if (current_tile[0] < 0 or current_tile[0] > 37) or (current_tile[1] < 0 or current_tile[1] > 50): continue

                # If the surrounding tile is a wall
                if dict_output[current_tile][1] == 1: continue

                # If it as already been processed
                if current_tile in processed_coords: continue

                # If it has already been processed by an other tile
                if current_tile in next_process: continue

                # If current tile is the exit
                if current_tile == entrance_cell_coords:
                    print(dict_output[coord])
                    is_searching = False
                    break

                # Mark the distance from the arrived
                dict_output[current_tile][4] = dict_output[coord][4] + 1
                dict_output[current_tile][5] = True
                next_process.append(current_tile)

                # Update the canvas
                color = colors[dict_output[current_tile][4]] if dict_output[current_tile][4] <= 399 else colors[-1]
                editor.main_canvas.itemconfigure(dict_output[current_tile][2], fill=color, outline=color)

                # Update the GUI
                editor.main_canvas.update()
                editor.update()
            
            if is_searching == False:
                break

            processed_coords.append(coord)

        coords_to_process = next_process.copy()
        next_process.clear()

    current_tile = entrance_cell_coords
    is_solving = True

    while is_solving:
        dict_output[current_tile][4] = 0
        current_process = {}

        for direction in direction_to_process:
            next_tile = (current_tile[0] + direction[0], current_tile[1] + direction[1])
            
            # If the tile is out of bound skip it
            if next_tile[0] < 0 or next_tile[0] > 37 or next_tile[1] < 0 or next_tile[0] > 50: continue
            
            # If the tile is the exit, stop the solving
            if dict_output[next_tile][3] == 1:
                is_solving = False
                break
            
            # If the tile hasn't been processed skip it
            if dict_output[next_tile][5] == False: continue
            
            current_process[next_tile] = (dict_output[next_tile][4], dict_output[next_tile][2])
        
        if not is_solving:
            break
        
        sorted_current_process = {k: v for k, v in sorted(current_process.items(), key=lambda item: item[1])}
        dict_output[current_tile][5] = False
        current_tile = list(sorted_current_process.items())[0][0]
        
        editor.main_canvas.itemconfig(dict_output[current_tile][2], fill='violet', outline='violet')
        editor.main_canvas.update()
        editor.update()
        
        
    editor.sim_data.can_generate = True
    editor.sim_data.can_solve = True
    print("Solved !")
    
    
