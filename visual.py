from tkinter import Tk, BOTH, Canvas

class Window():
    """An application window that can update.
    
    Attributes
        width (int): Width of the window in pixels
        height (int): Height of the window in pixels
        root (Tk): Root widget for Tkinter
        is_running (bool): Flag that indicates if a window is active
    """

    def __init__(self, width, height):
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


    def redraw(self):
        """Redraws the content of the window"""
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        """Continuously redraws the window"""
        self.is_running = True
        while self.is_running:
            self.redraw()


    def close(self):
        """Sets the is_running flag to false to stop redrawing the window"""
        self.is_running = False

