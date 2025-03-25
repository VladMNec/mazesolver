from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.point_a = a
        self.point_b = b

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_colour, width=2)


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._top_left = Point(self._x1, self._y1)
        self._bottom_left = Point(self._x1, self._y2)
        self._top_right = Point(self._x2, self._y1)
        self._bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            self._win.draw_line(Line(self._top_left, self._bottom_left), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(self._top_right, self._bottom_right), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(self._top_left, self._top_right), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(self._bottom_left, self._bottom_right), "black")

    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "gray"

        first_x = (self._x1 + self._x2) / 2
        first_y = (self._y1 + self._y2) / 2

        second_x = (to_cell._x1 + to_cell._x2) / 2
        second_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(first_x, first_y), Point(second_x, second_y))
        self._win.draw_line(line, colour)