from http.cookiejar import MozillaCookieJar
from re import X
from turtle import color
import numpy as np
from Algorithm.Solving.Solving_Util import *
from colour import Color
# from GUI.EditorGUI import Editor Only there for developpement shouldn't be there when launching because of circular import

red = Color("red")
colors_ = list(red.range_to(Color("purple"),2000))

# Return true if the cell is not a wall and not out of bound
def Is_Valid_Neighbor(coord: tuple, maze: dict, maze_shape: tuple) -> bool:
    # If the cell is out of bound
    if coord[0] < 0 or coord[0] >= maze_shape[1] or coord[1] < 0 or coord[1] >= maze_shape[0]: return False
    
    # If the cell is a wall
    if maze[coord][0][1] == 1: return False
    
    # If the cell has already been processed
    if not maze[coord][1] == 0: return False
    
    # If the cell has already been processed
    if maze[coord][4] == True: return False
        
    return True

# Same as Is_Valid_Neighbor but made for solving and not searching
def Is_Valid_Neighbor_(coord: tuple, maze: dict, maze_shape: tuple) -> bool:
    # If the cell is out of bound
    if coord[0] < 0 or coord[0] >= maze_shape[1] or coord[1] < 0 or coord[1] >= maze_shape[0]:
        return False
    
    # If the cell is a wall
    if maze[coord][0][1] == 1: 
        return False
    
    # If the cell has already been processed
    if maze[coord][1] == 0 or maze[coord][4] == False:
        return False
        
    return True

def Get_Node_G_Cost(neighbor_cell, current_cell) -> int:
    y_delta = abs(neighbor_cell[0] - current_cell[0]) 
    x_delta = abs(neighbor_cell[1] - current_cell[1])
    
    return (x_delta + y_delta) * 10

def Get_Node_H_Cost(current_cell, entrance_exit_distance) -> int:
    x_delta = abs(current_cell[1] - entrance_exit_distance[1])
    y_delta = abs(current_cell[0] - entrance_exit_distance[0])
    
    return round((((x_delta ** 2 + y_delta ** 2) ** 0.5) * 10) * (20 / 14))

Get_Node_F_Cost = lambda g_cost, h_cost: g_cost + h_cost

def Distance(a_coord, b_coord) -> int:
    x_delta = abs(a_coord[1] - b_coord[1])
    y_delta = abs(a_coord[0] - b_coord[0])
    
    return round((((x_delta ** 2 + y_delta ** 2) ** 0.5) * 10) * (20 / 14))

def Get_Identics(cell_list: dict) -> dict:
    output = {}
    
    for key in cell_list:
        if cell_list[key][3] == cell_list[list(cell_list.keys())[0]][3]:
            output[key] = cell_list[key]
            continue
        
        break
    
    return output

def Solve(editor: """Editor""", maze: np.array) -> None:
    Clear_Maze(maze, editor.main_canvas)
    
    maze_dict = Maze_To_Dict(maze, use_maze_value=False)
    
    entrance_cell = Get_Cell_Coord(editor.sim_data.entrance_cell.cell_id, maze.shape)
    exit_cell = Get_Cell_Coord(editor.sim_data.exit_cell.cell_id, maze.shape)
    
    distance_start_finish = Distance(entrance_cell, exit_cell)
    
    current_cell = exit_cell
    maze_dict[current_cell][4] = True
    calculated_cell = {}
    
    is_searching = True
    
    while is_searching:
        neighbours = []
        list_potential_neighbours = Get_Cell_Neighbours(current_cell)
        
        for potential_neighbour in list_potential_neighbours:
            if potential_neighbour == entrance_cell:
                is_searching = False
                break
            
            if Is_Valid_Neighbor(potential_neighbour, maze_dict, maze.shape):
                
                g_cost = Get_Node_G_Cost(potential_neighbour, current_cell)
                h_cost = Get_Node_H_Cost(potential_neighbour, entrance_cell)
                f_cost = Get_Node_F_Cost(g_cost, h_cost)
                
                maze_dict[potential_neighbour][1] = g_cost
                maze_dict[potential_neighbour][2] = h_cost
                maze_dict[potential_neighbour][3] = f_cost
                
                maze_dict[potential_neighbour][5] = current_cell
                
                calculated_cell[potential_neighbour] = maze_dict[potential_neighbour]
                
                editor.main_canvas.itemconfig(maze_dict[potential_neighbour][0][2], fill="lime", outline="lime")
        
        calculated_cell_ = Get_Identics({k: v for k, v in sorted(calculated_cell.items(), key=lambda item: item[1][3])})
        
        if not len(calculated_cell) == 1:
            calculated_cell_ = {k: v for k, v in sorted(calculated_cell.items(), key=lambda item: item[1][2])}
        
        current_cell = list(calculated_cell_.keys())[0]
        calculated_cell.pop(current_cell)
            
        maze_dict[current_cell][4] = True
        
        color = colors_[maze_dict[current_cell][0][2]] if maze_dict[current_cell][0][2] <= 1999 else colors_[-1]
        editor.main_canvas.itemconfig(maze_dict[current_cell][0][2], fill=color, outline=color)
        
        editor.main_canvas.update()
        editor.update()
    
    not_solved = True
    current_cell = entrance_cell
    
    neighbours = {}
    potential_neighbours = Get_Cell_Neighbours(current_cell)
        
    for potential_neighbour in potential_neighbours:
        if potential_neighbour == exit_cell:
            not_solved = False
            break
            
        if Is_Valid_Neighbor_(potential_neighbour, maze_dict, maze.shape):
            neighbours[potential_neighbour] = maze_dict[potential_neighbour]
    
    current_cell = list(neighbours.keys())[0]
    
    while not_solved:
        for potential_neighbour in Get_Cell_Neighbours(current_cell):
            if potential_neighbour == exit_cell:
                not_solved = False
                break
        
        if not not_solved:
            break
        
        current_cell = maze_dict[current_cell][5]
        
        editor.main_canvas.itemconfig(maze_dict[current_cell][0][2], fill='violet', outline='violet')
        
        editor.main_canvas.update()
        editor.update()
        
        