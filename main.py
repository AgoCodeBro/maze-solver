from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main() -> None:
    """Creates a 800x600 pixel window and a maze grid and displays them untill the user closes it."""
    win = Window(800, 600)
    maze = Maze(3, 3, 10, 10, 25, 25, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)

    win.wait_for_close()  

if __name__ == "__main__":
    main()

    