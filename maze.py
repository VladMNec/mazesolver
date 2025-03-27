from panel import Cell
import time

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for col in range(self._num_cols):
            new_list = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                new_list.append(cell)
            self._cells.append(new_list)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                if (col == 0 and row == 0) or (col == self._num_cols - 1 and row == self._num_rows - 1):
                    self._break_entrance_and_exit(col, row)
                else:
                    self._draw_cell(col, row)

                
    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = self._cell_size_x + x1
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = self._cell_size_y + y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _break_entrance_and_exit(self, i, j):
        if self._num_rows == 1 and self._num_cols == 1:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j].has_bottom_wall = False
        elif i == 0 and j == 0:
            self._cells[i][j].has_top_wall = False
        else:
            self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)


    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.03)
