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
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__top_left = Point(self.__x1, self.__y1)
        self.__bottom_left = Point(self.__x1, self.__y2)
        self.__top_right = Point(self.__x2, self.__y1)
        self.__bottom_right = Point(self.__x2, self.__y2)

        if self.has_left_wall:
            self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "black")