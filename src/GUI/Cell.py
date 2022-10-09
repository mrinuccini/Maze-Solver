from tkinter import Canvas

# A maze cell
class Cell:
    cell_id = 0
    is_wall = False
    canvas_object_id = 0

    def __init__(self, cell_id: int, canvas: Canvas, x_pos: int, y_pos: int,  dimensions: int=10) -> None:
        color = 'white' if cell_id % 2 == 0 else 'gray'
        self.canvas_object_id = canvas.create_rectangle(x_pos, y_pos, x_pos + dimensions, y_pos + dimensions,
            fill=color, outline=color)
        self.cell_id = cell_id