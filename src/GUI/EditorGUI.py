from tkinter import *
from GUI.Cell import Cell
from GUI.Simulation_Data import Simulation_Data

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

    # Use to change the state of a cell when creating a maze
    def On_Canvas_Click(self, event) -> None:
        cell_id = event.widget.find_closest(event.x, event.y)[0] - 1

        # If the current cell id is the same as last don't do anything
        if self.last_click_event == cell_id: return

        # If the cell is not a wall then make it a wall howerver make it a classic cell
        cell = self.sim_data.cell_list[cell_id]
        cell.is_wall = not cell.is_wall
        self.main_canvas.itemconfig(cell.canvas_object_id, fill='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray',
            outline='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray')

        # Store the current cell's id
        self.last_click_event = cell_id

    # Use to draw the canvas where the maze will be generated and solved
    def DrawCanvas(self) -> None:
        self.main_canvas = Canvas(self, width=1327, height=750, bg='black')

        # Generate the grid of cells
        current_cell_id = 0

        for y in range(0, 750, self.sim_data.cell_dim):
            for x in range(0, 1330, self.sim_data.cell_dim):
                cell = Cell(current_cell_id, self.main_canvas, x_pos=x, y_pos=y, dimensions=self.sim_data.cell_dim)
                self.sim_data.cell_list.append(cell)

                current_cell_id += 1

        # Bind the paint event
        self.main_canvas.bind('<B1-Motion>', lambda event: self.On_Canvas_Click(event))

        self.main_canvas.pack()
        cell_list = self.sim_data.Export_Cell_List()
        print(cell_list.shape)