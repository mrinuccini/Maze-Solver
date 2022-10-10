from os import curdir
from GUI.Cell import Cell
import numpy as np

class Simulation_Data:
    cell_dim = 15
    cell_list = []
    entrance_cell: Cell = None
    exit_cell: Cell = None

    def __init__(self, cell_dim: int):
        self.cell_dim = cell_dim

    def Export_Cell_List(self) -> list:
        binary_list = [(cell.cell_id, 1 if cell.is_wall else 0, cell.canvas_object_id, cell.attribute, -1) for cell in self.cell_list]
        binary_array = np.array(binary_list).reshape((51, 38, 5))

        return binary_array