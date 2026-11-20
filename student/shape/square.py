from shape.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    def __str__(self):
        return f"Shape: {self.name} (side: {self.width})"