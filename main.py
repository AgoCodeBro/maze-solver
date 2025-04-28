from window import Window
from line import Line
from point import Point
from cell import Cell


def main() -> None:
    """Creates a 800x600 pixel window and some cells and displays them untill the user closes it."""
    win = Window(800, 600)
    cells = []

    
    top_left = Point(2, 2)
    bottom_right = Point(52, 52)

    for i in range(4):
        cells.append(Cell(top_left, bottom_right, win))
        top_left = Point(top_left.x + 50, top_left.y)
        bottom_right = Point(bottom_right.x + 50, bottom_right.y)

    cells[0].has_left_wall = False
    cells[1].has_top_wall = False
    cells[2].has_bottom_wall = False
    cells[3].has_right_wall = False

    for cell in cells:
        cell.draw()

    win.wait_for_close()

 
    
    

if __name__ == "__main__":
    main()

    