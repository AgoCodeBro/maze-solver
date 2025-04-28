from tkinter import Tk, BOTH, Canvas
from line import Line

class Window():
    """An application window that can update.
    
    Attributes
        width (int): Width of the window in pixels
        height (int): Height of the window in pixels
        root (Tk): Root widget for Tkinter
        is_running (bool): Flag that indicates if a window is active
    """

    def __init__(self, width: int, height: int) -> None:
        """Creates a new window instance.
        
        Args:
            width (int): Width of the window
            height (int): Height of the window
        """
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("root widget")
        self.canvas = Canvas(self.root)

        self.canvas.pack()

        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self) -> None:
        """Redraws the content of the window."""
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self) -> None:
        """Continuously redraws the window."""
        self.is_running = True
        while self.is_running:
            self.redraw()


    def close(self) -> None:
        """Sets the is_running flag to false to stop redrawing the window."""
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        """Draws a line of the given color.
        
        Args:
            line (Line): 2D representation of the line to be drawn
            fill_color (str): Color of the line
        """
        line.draw(self.canvas, fill_color)

