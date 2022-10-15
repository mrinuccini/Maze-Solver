from tkinter import *
from tkinter.messagebox import showinfo
from GUI.Cell import Cell
from GUI.Simulation_Data import Simulation_Data
from Algorithm.Solving.Breadth_First import Solve as Breadth_First_Solve
from Algorithm.Generation.Kruskal_Algorithm import Generate_Maze as Krustal_Generate
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
        self.geometry("1320x780")

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
        # Checks if a generation or a solving is not in progress
        if not self.sim_data.can_generate:
            showinfo("Warning", "Cannot clear the canvas while a generation or a solving is in progress.")
            return
        
        for cell in self.sim_data.cell_list:
            if not cell.attribute == 0: continue
            
            cell.is_wall = False
            self.main_canvas.itemconfig(cell.canvas_object_id, fill='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray',
            outline='black' if cell.is_wall else 'white' if cell.cell_id % 2 == 0 else 'gray')

    # Use to draw the canvas where the maze will be generated and solved
    def DrawCanvas(self) -> None:
        self.main_canvas = Canvas(self, width=1020, height=780, bg='black')

        # Generate the grid of cells
        current_cell_id = 0

        for y in range(0, 780, self.sim_data.cell_dim):
            for x in range(0, 1020, self.sim_data.cell_dim):
                cell = Cell(current_cell_id, self.main_canvas, x_pos=x, y_pos=y, dimensions=self.sim_data.cell_dim)
                self.sim_data.cell_list.append(cell)

                current_cell_id += 1

        # Pick the entrance and exit cell
        entrance_cell = self.sim_data.cell_list[52]
        exit_cell = self.sim_data.cell_list[1936]

        exit_cell.attribute = 1
        entrance_cell.attribute = 2

        self.sim_data.entrance_cell = entrance_cell
        self.sim_data.exit_cell = exit_cell

        # Give them color
        self.main_canvas.itemconfig(exit_cell.canvas_object_id, fill='green', outline='green')
        self.main_canvas.itemconfig(entrance_cell.canvas_object_id, fill='blue', outline='blue')
        
        # Add icon to the entrance and exit cell
        entrance_icon = PhotoImage(file="src/GUI/assets/start.png")
        self.main_canvas.create_image(20, 20, image=entrance_icon, anchor=NW)
        
        exit_icon = PhotoImage(file="src/GUI/assets/exit.png")
        self.main_canvas.create_image(980, 740, image=exit_icon, anchor=NW)

        # Bind the paint event
        self.main_canvas.bind('<B1-Motion>', lambda event: self.On_Canvas_Click(event, True))
        self.main_canvas.bind('<Button-1>', lambda event: self.On_Canvas_Click(event, False))

        self.main_canvas.pack(side=RIGHT)

    def Draw_Left_Pannel(self) -> None:
        # A title for the algorithm (generation) dropdown
        self.generation_algorithm_title = Label(self, text="Generation Algorithm", font=("Arial", 20))
        self.generation_algorithm_title.place(x=20, y=0)
        
        # The dropbox to choose the maze generation algorithm
        generation_options = ["Kruskal's algorithm"]
        
        choice_generation = StringVar(self)
        choice_generation.set(generation_options[0])
        
        self.generation_algorithm_choice = OptionMenu(self, choice_generation, *generation_options)
        self.generation_algorithm_choice.place(x=20, y=40)
        
        # A title for the algorithm (solving) dropdown
        self.generation_algorithm_title = Label(self, text="Solving Algorithm", font=("Arial", 20))
        self.generation_algorithm_title.place(x=20, y=70)
        
        # The dropbox to choose the maze generation algorithm
        options_solving = ["Breadth-First"]
        
        choice_solving = StringVar(self)
        choice_solving.set(options_solving[0])
        
        self.generation_algorithm_choice = OptionMenu(self, choice_solving, *options_solving)
        self.generation_algorithm_choice.place(x=20, y=110)
        
        # The button to solve the maze
        self.solve_button = Button(self, text="Solve", font=("Arial", 20), command=lambda: Breadth_First_Solve(self.sim_data, self, self.sim_data.Export_Cell_List()))
        self.solve_button.place(x=20, y=140)

        # The button to clear the maze
        self.clear_button = Button(self, text="Clear", font=("Arial", 20), command=lambda: self.Clear_Canvas())
        self.clear_button.place(x=20, y=180)
        
        # The button to generate a maze
        self.generate_button = Button(self, text="Generate", font=("Arial", 20), command=lambda: Krustal_Generate((51, 39), self))
        self.generate_button.place(x=20, y=220)