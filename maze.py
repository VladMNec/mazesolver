from panel import Cell
import time
import random

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for col in range(self._num_cols):
            new_list = []
            for row in range(self._num_rows):
                new_list.append(Cell(self._win))
            self._cells.append(new_list)

                
    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = self._cell_size_x + x1
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = self._cell_size_y + y1
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].has_bottom_wall = False
        self._cells[0][0].has_right_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_left_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    
    def _break_walls_r(self, i, j):
        print(f"Breaking walls at cell ({i}, {j})")
        self._cells[i][j].visited = True
        while True:
            cell_list = []
            # check left
            if i > 0 and self._cells[i - 1][j].visited == False:
                cell_list.append((i - 1, j))
            # check right
            if i < self._num_cols - 1 and self._cells[i + 1][j].visited == False:
                cell_list.append((i + 1, j))
            # check up
            if j > 0 and self._cells[i][j - 1].visited == False:
                cell_list.append((i, j - 1))
            #check down
            if j < self._num_rows - 1 and self._cells[i][j + 1].visited == False:
                cell_list.append((i, j + 1))
            if len(cell_list) == 0:
                self._draw_cell(i, j)
                return
            # random direction
            next_cell = cell_list[random.randint(0, len(cell_list) - 1)]
            # new direction indices
            new_i, new_j = next_cell[0], next_cell[1]

            if new_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][j].has_left_wall = False
            if new_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][j].has_right_wall = False
            if new_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][new_j].has_top_wall = False
            if new_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][new_j].has_bottom_wall = False
            self._break_walls_r(new_i, new_j)


    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.03)
