from panel import *

win = Window(800, 600)
cell = Cell(win)
cell.draw(50, 50, 100, 100)
win.draw_line(Line(Point(50, 60), Point(240, 130)), "red")
win.draw_line(Line(Point(124, 543), Point(720, 480)), "black")
win.wait_for_close()
