from concurrent.futures.process import _chain_from_iterable_of_lists
from tkinter import Canvas
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
                    math.ceil((cell_ratio - math.floor(cell_ratio)) * shape[0])
                  )
    return cell_coords

def Solve(sim_data: Simulation_Data, canvas: Canvas, maze: np.array):
    print("Solving Maze...")
    dict_output = {}

    """ Generate a dictionnary with key being coordinates and values being cell data """
    for x in range(0, maze.shape[0]):
        for y in range(0, maze.shape[1]):
            dict_output[Get_Cell_Coord(maze[x][y][0], maze.shape)] = maze[x][y]
    
    print(dict_output[(37, 50)])
    print("Solved !")
    
    
