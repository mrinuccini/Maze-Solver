from tkinter import *
from GUI.Cell import Cell
from GUI.Simulation_Data import Simulation_Data
from Algorithm.Solving.Dimensions_Code_Algorithm import Solve as Dimension_Code_Solve
import numpy as np
import random

class Editor(Tk):
    sim_data = None
    last_click_event = 0

    # Function to initialize everything
    def __init__(self) -> None:
        # Initialize variables and the tkinter super
        super().__init__()
        self.sim_data = Simulation_Data(20)

        self.title("SquidyDev Maze Solver")
        self.geometry("1320x760")

        self.DrawCanvas()
        self.Draw_Left_Pannel()

    # Use to change the state of a cell when creating a maze
    def On_Canvas_Click(self, event, drag) -> None:
        cell_id = event.widget.find_closest(event.x, event.y)[0] - 1

        # If the current cell id is the same as last don't do anything (only if we are dragging)
        if drag and self.last_click_event == cell_id: return

        # If the cell is not a wall then make it a wall howerver make it a classic cell
        cell = self.sim_data.cell_list[cell_id]
        cell.is_wall = not cell.is_wall
        self.main_canvas.itemconfig(cell.canvas_object_id, fill='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray',
            outline='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray')

        # Store the current cell's id if we are dragging
        if drag:
            self.last_click_event = cell_id

    # Use to clear the canvas
    def Clear_Canvas(self) -> None:
        for cell in self.sim_data.cell_list:
            if not cell.attribute == 0: continue
            
            cell.is_wall = False
            self.main_canvas.itemconfig(cell.canvas_object_id, fill='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray',
            outline='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray')

    # Use to draw the canvas where the maze will be generated and solved
    def DrawCanvas(self) -> None:
        self.main_canvas = Canvas(self, width=1020, height=760, bg='black')

        # Generate the grid of cells
        current_cell_id = 0

        for y in range(0, 750, self.sim_data.cell_dim):
            for x in range(0, 1020, self.sim_data.cell_dim):
                cell = Cell(current_cell_id, self.main_canvas, x_pos=x, y_pos=y, dimensions=self.sim_data.cell_dim)
                self.sim_data.cell_list.append(cell)

                current_cell_id += 1

        entrance_cell = self.sim_data.cell_list[random.randint(0, len(self.sim_data.cell_list))]
        exit_cell = self.sim_data.cell_list[random.randint(0, len(self.sim_data.cell_list))]

        exit_cell.attribute = 1
        entrance_cell.attribute = 2

        self.sim_data.entrance_cell = entrance_cell
        self.sim_data.exit_cell = exit_cell

        self.main_canvas.itemconfig(exit_cell.canvas_object_id, fill='green', outline='green')
        self.main_canvas.itemconfig(entrance_cell.canvas_object_id, fill='blue', outline='blue')

        # Bind the paint event
        self.main_canvas.bind('<B1-Motion>', lambda event: self.On_Canvas_Click(event, True))
        self.main_canvas.bind('<Button-1>', lambda event: self.On_Canvas_Click(event, False))

        self.main_canvas.pack(side=RIGHT)

    def Draw_Left_Pannel(self) -> None:
        self.solve_button = Button(self, text="Solve", font=("Arial", 20), command=lambda: Dimension_Code_Solve(self.sim_data, self, self.sim_data.Export_Cell_List()))
        self.solve_button.pack(side=LEFT)

        self.clear_button = Button(self, text="Clear", font=("Arial", 20), command=lambda: self.Clear_Canvas())
        self.clear_button.pack(side=LEFT)