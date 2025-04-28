from visual import Window
from lines import Point, Line


def main() -> None:
    """Creates and displays a 800x600 pixel window and a black line until the user closes it."""
    win = Window(800, 600)

    start = Point(0,0)
    end = Point(100, 100)

    line = Line(start, end)
    win.draw_line(line, "black")

    win.wait_for_close()

 
    
    

if __name__ == "__main__":
    main()

    