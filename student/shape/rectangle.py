from shape.shape import Shape


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"{super().__str__()} ({self.width} x {self.height})"