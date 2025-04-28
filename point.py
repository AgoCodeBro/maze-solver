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

    def __repr__(self) -> str:
        """Returns a string representation of the point"""
        result = f"""Point
--------
X: {self.x}
Y: {self.y}
"""
        return result