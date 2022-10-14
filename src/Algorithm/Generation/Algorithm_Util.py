from Algorithm.Solving.Dimensions_Code_Algorithm import Get_Cell_Coord
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
    editor.update()
    editor.main_canvas.update()