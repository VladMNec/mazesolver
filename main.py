from panel import *
from maze import *

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw(100, 50, 150, 100)
    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell3.draw(100, 100, 150, 150)
    cell2.draw_move(cell3, undo=True)

    win.wait_for_close()


main()
