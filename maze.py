from cell import Cell
from point import Point
from window import Window
import time
import random

class Maze():
    """Representaion of the maze made up of a grid of cells
    
    Attributes:
        start (Point): What point should the maze start be
        num_rows (int): Number of rows of cells the maze has
        num_cols (int): Number of columns of cells the maze has
        cell_size_x (int): Width of each cell in pixels
        cell_size_y (int): Height of each cell in pixels
        win (Window): Window on which the maze should be drawn
    """
    
    def __init__(self, start_x: int, start_y: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int | None = None, win: Window | None = None, seed: int | None = None) -> None:
        """Creates an instance of a maze
        
        Args:
            start_x (int): What x coordinat the maze start should be
            start_y (int): What y coordinat the maze start should be
            num_rows (int): Number of rows of cells the maze has
            num_cols (int): Number of columns of cells the maze has
            cell_size_x (int): Width of each cell in pixels
            cell_size_y (int): Height of each cell in pixels. If None, it is set equal to cell_size_x
            win (Window): Window on which the maze should be drawn. If none, logic will run it wont be displayed
            seed (int): Sets the seed for the maze. If None, selects seed at random
            _cells (List[List[Cell]]): A 2d list of cells that represents the maze
        """

        self.start = Point(start_x, start_y)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x

        if cell_size_y is None:
            self.cell_size_y = cell_size_x

        else:
            self.cell_size_y = cell_size_y

        self.win = win
        random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self) -> None:
        """Populates the _cells attribute"""

        for i in range(self.num_cols):
            self._cells.append([])

            for j in range(self.num_rows):
                top_left_x = self.start.x + (i * self.cell_size_x)
                top_left_y = self.start.y + (j * self.cell_size_y)
                top_left = Point(top_left_x, top_left_y)
                
                bottom_right_x = top_left_x + self.cell_size_x
                bottom_right_y = top_left_y + self.cell_size_y
                bottom_right = Point(bottom_right_x, bottom_right_y)

                self._cells[i].append(Cell(top_left, bottom_right, self.win))
                self._draw_cell(i, j)
                
    def _draw_cell(self, i: int, j: int) -> None:
        """Draws the cell at grid positon i, j where 0,0 is the top right corner"""
        if self.win is None:
            return
        
        self._cells[i][j].draw()
        self._animate()

    def _animate(self) -> None:
        """Draws the maze with a delay so that the user can see what is happening"""
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        """Breaks the top wall of the top left cell and the bottom wall of the bottom
        right cell creating the start and exit
        """
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False

        self._draw_cell(0,0)
        self._draw_cell(self.num_cols - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        """Recursivley breaks wall to create a maze"""
        self._cells[i][j].visited = True
        keep_going = True

        while keep_going:
            to_visit = []
            directions = {"up" : (i, j - 1 ),
                          "down" : (i, j + 1),
                          "left" : (i - 1, j),
                          "right" : (i + 1, j)}
    
            for key in directions:
                direction = directions[key]
                x = direction[0]
                y = direction[1] 

                # If the direction is within the grid
                if x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows:

                    if not self._cells[x][y].visited:
                        to_visit.append(key)

            # If there are no valid options, stop looping
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                keep_going = False

            # Else select one at random and destroy walls between
            else:
                index = random.randrange(len(to_visit))

                direction = to_visit[index]
                x = directions[direction][0]
                y = directions[direction][1]
                
                if direction == "up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[x][y].has_bottom_wall = False

                if direction == "down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[x][y].has_top_wall = False

                if direction == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[x][y].has_right_wall = False


                if direction == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[x][y].has_left_wall = False

                self._break_walls_r(x, y)

    def _reset_cells_visited(self) -> None:
        """Set visited to false for all cells"""
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self) -> bool:
        """Visually solves the maze.
        
        Return True if maze is solved and False if it is not
        """
        return self.solve_r(0,0)

    def solve_r(self, i, j) -> bool:
        """Recursively solves the maze while drawing the path
        
        Args:
            i (int): Current x position in the maze
            j (int): Current y position in the maze
        """
        if i == self.num_cols - 1 and j == self.num_rows -1:
            return True
        
        cur_cell = self._cells[i][j]
        cur_cell.visited = True
        neighbors = self.get_neighbors(cur_cell, i, j)
        directions = {"up" : (i, j - 1 ),
                      "down" : (i, j + 1),
                      "left" : (i - 1, j),
                      "right" : (i + 1, j)}
        
        if len(neighbors) == 0:
            return False

        for direction in neighbors:
            x = directions[direction][0]
            y = directions[direction][1]
            next_cell =  self._cells[x][y]
            if not next_cell.visited:
                cur_cell.draw_move(next_cell)
                self._animate()
                result = self.solve_r(x, y)
                if result:
                    return True

                else:
                    cur_cell.draw_move(next_cell, undo=True)
                    self._animate()
                
 

            

        return False
    
    def get_neighbors(self, cur_cell: Cell, i: int, j: int) -> list[str]:
        """Returns a list with valid directions you can go in maze from a given cell
        
        Args:
            cur_cell (Cell): The cell we are finding the neighbors of
            i (int): Current x position in the maze
            j (int): Current y position in the maze

        Returns list containg strings of directions you can move
        """
        neighbors = []

        if not cur_cell.has_top_wall and j > 0:
            neighbors.append("up")

        if not cur_cell.has_bottom_wall and j < self.num_rows - 1:
            neighbors.append("down")
            
        if not cur_cell.has_left_wall and i > 0:
            neighbors.append("left")
            
        if not cur_cell.has_right_wall and i < self.num_cols - 1 :
            neighbors.append("right")

        return neighbors
            






            

            
