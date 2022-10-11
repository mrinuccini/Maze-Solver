"""

This is a test unit that allow you to click on a tile of the maze and coords of the tile will print in the console

"""

""" Section to allow test modules to use code from source directory """
import sys
import os
path = os.getcwd()
sys.path.insert(1, f'{path}/src/')
""" End section to allow test modules to use code from source directory """

from GUI.EditorGUI import Editor
import math

def Print_Cell_Coords(event):
    cell_id = event.widget.find_closest(event.x, event.y)[0] - 1
    print(cell_id)

    cell_y_ratio = cell_id / 51
    cell_coords = (math.floor(cell_y_ratio),
                   round((cell_y_ratio - math.floor(cell_y_ratio)) * 51)
                  )
    print(cell_coords)

def main():
    editor = Editor()
    
    editor.main_canvas.bind("<Button-1>", lambda event: Print_Cell_Coords(event))

    editor.mainloop()

if __name__ == "__main__":
    main()