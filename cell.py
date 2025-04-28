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
        visited (bool): Flag to indicate if walls for the cell have been broken 
            while genereating the maze
    """

    def __init__(self, top_left: Point, bottom_right: Point, win: Window | None = None) -> None:
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
        self.visited = False

    def __repr__(self) -> str:
        """Returns a string representation of the cell"""
        result =  f"""Cell
----------
Top Left: {self.top_left}
Top Right: {self.top_right}
Bottom Left: {self.bottom_left}
Bottom Right: {self.bottom_right}
Right Wall: {self.has_right_wall}
Left Wall: {self.has_left_wall}
Top Wall: {self.has_top_wall}
Bottom Wall: {self.has_bottom_wall}
"""
        return result

    
    def draw(self) -> None:
        """Draws the cell on its window's canvas"""
        if self.win is None:
            return

        if self.has_left_wall:
            line = Line(self.top_left, self.bottom_left)
            self.win.draw_line(line, "black")
        
        else:
            line = Line(self.top_left, self.bottom_left)
            self.win.draw_line(line, "#d9d9d9")
        
        if self.has_right_wall:
            line = Line(self.top_right, self.bottom_right)
            self.win.draw_line(line, "black")

        else:
            line = Line(self.top_right, self.bottom_right)
            self.win.draw_line(line, "#d9d9d9")
        
        if self.has_top_wall:
            line = Line(self.top_left, self.top_right)
            self.win.draw_line(line, "black")

        else:
            line = Line(self.top_left, self.top_right)
            self.win.draw_line(line, "#d9d9d9")
        
        if self.has_bottom_wall:
            line = Line(self.bottom_left, self.bottom_right)
            self.win.draw_line(line, "black")

        else:
            line = Line(self.bottom_left, self.bottom_right)
            self.win.draw_line(line, "#d9d9d9")


    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        """Draws a line from the center of the current cell to the center of the destination cell
        
        Args:
            to_cell (Cell): The cell the move is going to
            undo (Bool): Flag to denote we are undoing a move and change the color of the line accordingly
        """
        if undo:
            color = "grey"

        else:
            color = 'red'

        cur_center = self.center()
        to_center = to_cell.center()
        path = Line(cur_center, to_center)

        self.win.draw_line(path, color)

        

    def center(self) -> Point:
        """Calculates the point at the center of the cell and returns it
        
        Returns:
            Point: Represents center of cell rounded down to nearest pixel
        """
        cur_mid_x = (self.top_left.x + self.bottom_right.x) // 2
        cur_mid_y = (self.top_left.y + self.bottom_right.y) // 2

        return Point(cur_mid_x, cur_mid_y)
    



