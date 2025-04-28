import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(4, 4, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(4, 4, num_rows, num_cols, 10, 10)
        
        m1._break_entrance_and_exit()

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[11][9].has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(4, 4, num_rows, num_cols, 10, 10)

        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()

        for column in m1._cells:
            for cell in column:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()