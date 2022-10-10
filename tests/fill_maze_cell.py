""" Section to allow test modules to use code from source directory """
import sys
import os
path = os.getcwd()
sys.path.insert(1, f'{path}/src/')
""" End section to allow test modules to use code from source directory """

from GUI.EditorGUI import Editor
import time
import numpy as np

def main():
    editor = Editor()
    maze = editor.sim_data.Export_Cell_List()
    print(f"Maze shape {maze.shape}")
    
    for x in range(0, maze.shape[0]):
        for y in range(maze.shape[1]):
            if not maze[x][y][3] == 0:
                continue

            editor.main_canvas.itemconfig(maze[x][y][2], fill='green', outline='green')

            editor.main_canvas.update()
            editor.update()

            time.sleep(0.00001)

    editor.mainloop()

if __name__ == "__main__":
    main()