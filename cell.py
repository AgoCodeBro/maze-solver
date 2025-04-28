from point import Point
from line import Line
from window import Window

class Cell():
    """Repesentation of a cell in a grid.
    
    Each cell has the potential to have up to 4 walls, and we will be allowed to travel between adjacent cells if
    no wall is blockin the path.

    Attributes:
        top_left (Point): Gives position of top left corner
        top_right (Point): Gives position of top right corner
        bottom_left (Point): Gives position of bottom left corner
        bottom_right (Point): Gives position of bottom right corner
        has_left_wall (bool): Flag indicates if left wall is present
        has_right_wall (bool): Flag indicates if right wall is present
        has_top_wall (bool): Flag indicates if top wall is present
        has_bottom_wall (bool): Flag indicates if bottom wall is present
        win (Window): The window that has the canvase where cell will be drawn on
    """

    def __init__(self, top_left: Point, bottom_right: Point, win: Window) -> None:
        """Creates an instance of the Cell class and gives it all 4 walls by default
        
        Args:
            top_left (Point): Gives position of top left corner
            bottom_right (Point): Gives position of bottom right corner
            win (Window): The window that has the canvas where cell will be drawn on
        """
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.top_right = Point(bottom_right.x, top_left.y)
        self.bottom_left = Point(top_left.x, bottom_right.y)
        self.win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    
    def draw(self) -> None:
        """Draws the cell on its window's canvas"""

        if self.has_left_wall:
            line = Line(self.top_left, self.bottom_left)
            self.win.draw_line(line, "black")
        
        if self.has_right_wall:
            line = Line(self.top_right, self.bottom_right)
            self.win.draw_line(line, "black")
        
        if self.has_top_wall:
            line = Line(self.top_left, self.top_right)
            self.win.draw_line(line, "black")
        
        if self.has_bottom_wall:
            line = Line(self.bottom_left, self.bottom_right)
            self.win.draw_line(line, "black")
        