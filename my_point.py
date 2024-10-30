import math

class MyPoint:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def calc_len(self):
        return math.sqrt(self.x**2 + self.y**2)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show_coord(self):
        print(f"Point {self.name}: ({self.x}, {self.y})")
