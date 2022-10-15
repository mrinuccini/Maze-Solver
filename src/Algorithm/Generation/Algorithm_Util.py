from Algorithm.Solving.Breadth_First import Get_Cell_Coord
from colour import Color

red = Color("red")
colors = list(red.range_to(Color("violet"),500))
colors.append("#FFFFFF")

# Use to display the maze to the viewport
def Display_Maze(maze: dict, editor, shape: tuple) -> None:
    for i in range(0, len(maze)):
        cell_coord = Get_Cell_Coord(i, shape)
        editor.sim_data.cell_list[i].is_wall = True if maze[cell_coord] == -1 else False
        
        if editor.sim_data.cell_list[i].is_wall:
            editor.main_canvas.itemconfig(editor.sim_data.cell_list[i].canvas_object_id, fill='black', outline='black')
        else:
            color = colors[maze[cell_coord] if maze[cell_coord] <= 499 else 499] if not maze[cell_coord] == -2 else colors[-1]
            editor.main_canvas.itemconfig(editor.sim_data.cell_list[i].canvas_object_id, fill=color, outline=color)
    editor.main_canvas.update()
    editor.update()
    
def Get_Neighbours_Cells(current_cell: tuple, maze: dict, shape: tuple, distance: int = 1) -> None:
    right = (current_cell[0] + distance, current_cell[1])
    left = (current_cell[0] - distance, current_cell[1])
    top = (current_cell[0], current_cell[1] - distance)
    bottom = (current_cell[0], current_cell[1] + distance)
    
    return [right, left, top, bottom]

def Fill_Maze(maze_shape: tuple) -> dict:
    maze = {}
    
    for x in range(0, maze_shape[0]):
        for y in range(0, maze_shape[1]):
            maze[(y, x)] = -1
            
    return maze

def Fill_Grid(maze_shape: tuple) -> dict:
    grid = {}
    
    for x in range(0, maze_shape[0]):
        for y in range(0, maze_shape[1]):
            grid[(y, x)] = 0
            
    return grid

def Get_Cell(coord: tuple, maze_shape: tuple, grid: dict):
    if coord[0] < 0 or coord[0] >= maze_shape[1] or coord[1] < 0 or coord[1] >= maze_shape[0]: return -2
    
    return grid[coord]

def Display_Exit_Entrace(editor):
    # Redraw the exit and entrance
    editor.main_canvas.itemconfig(editor.sim_data.entrance_cell.canvas_object_id, fill="blue", outline="blue")
    editor.main_canvas.itemconfig(editor.sim_data.exit_cell.canvas_object_id, fill="green", outline="green")