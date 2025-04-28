class Point():
    """2D point in the window using x and y coordinates.
    
    0 for the x axis represents the left side of the screen (increasing towards the right)
    and 0 for the y axis represents the top of the screen (increasing towards the bottom)

    Attributes:
        x (int): Distance from the left edge in pixels
        y (int): Distance from the top edge in pixels
    """

    def __init__(self, x, y) -> None:
        """Creates an instance of a point.
        
        Args:
            x (int): Distance from the left edge in pixels
            y (int): Distance from the top edge in pixels
        """
        self.x = x
        self.y = y


class Line():
    """2D Representaion of a line
    
    Attributes:
        start (Point): Point object representing the start point of the line
        end (Point): Point object representing the end point of the line
    """


    def __init__(self, start, end) -> None:
        """Creats an instance of the Line class
        
        Args:
            start (Point): Point object representing the start point of the line
            end (Point): Point object representing the end point of the line
        """
        self.start = start
        self.end = end

    
    def draw(self, canvas, fill_color) -> None:
        """Draws a 2px wide line of the specifed color on the given canvas
        
        Args:
            canvas (Canvas): Canvas to draw the line one
            fill_color (str): Color of the line
        """
        LINE_WIDTH = 2
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=LINE_WIDTH)
