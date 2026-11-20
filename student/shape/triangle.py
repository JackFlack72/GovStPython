from shape.shape import Shape


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{super().__str__()} (base: {self.base}, height: {self.height})"