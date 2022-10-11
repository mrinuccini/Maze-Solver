from concurrent.futures.process import _chain_from_iterable_of_lists
from GUI.Simulation_Data import Simulation_Data
from colour import Color
import math
import numpy as np

red = Color("red")
colors = list(red.range_to(Color("violet"),100))

# Returns a table containing the coords of the cell based on the shape of the table
def Get_Cell_Coord(cell_id, shape):
    cell_ratio = cell_id / shape[0]
    cell_coords = ( math.floor(cell_ratio),
                    round((cell_ratio - math.floor(cell_ratio)) * shape[0])
                  )
    return cell_coords

def Solve(sim_data: Simulation_Data, editor, maze: np.array):
    print("Solving Maze...")
    dict_output = {}
    count = 0


    """ Generate a dictionnary with key being coordinates and values being cell data """
    for x in range(0, maze.shape[0]):
        for y in range(0, maze.shape[1]):
            dict_output[Get_Cell_Coord(maze[x][y][0], maze.shape)] = maze[x][y]
            count += 1

    print(f"Length of dict : {len(dict_output)} ; expected length : {count}")

    entrance_cell_coords = Get_Cell_Coord(sim_data.entrance_cell.cell_id, maze.shape)
    exit_cell_coords = Get_Cell_Coord(sim_data.exit_cell.cell_id, maze.shape)
    direction_to_process = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    coords_to_process = [exit_cell_coords]
    next_coords = []
    processed_coords = []
    is_searching = True

    while is_searching:
        for coord in coords_to_process:
            for direction in direction_to_process:
                current_tile_coords = (coord[0] + direction[0], coord[1] + direction[1])

                if current_tile_coords == entrance_cell_coords: 
                    is_searching = False
                    break

                if (current_tile_coords[0] < 0 or current_tile_coords[1] < 0) or (current_tile_coords[0] > 37 or current_tile_coords[1] > 50) or current_tile_coords in processed_coords or dict_output[current_tile_coords][1] == 1: 
                    continue

                dict_output[current_tile_coords][4] = dict_output[coord][4] + 1
                editor.main_canvas.itemconfig(dict_output[current_tile_coords][2], fill=colors[dict_output[current_tile_coords][4]], outline=colors[dict_output[current_tile_coords][4]])

                # Append this code to the next coords to process
                next_coords.append(current_tile_coords)

            if not is_searching: break

            # Update the canvas and the tkinter window
            editor.main_canvas.update()
            editor.update()

            coords_to_process.remove(coord)
            # This coord has been process so we don't have to reprocess it later
            processed_coords.append(coord)

        # Update the list containing the next coords to process
        coords_to_process = coords_to_process.clear()
        coords_to_process = next_coords

        print(coords_to_process)
    print("Solved !")
    
    
