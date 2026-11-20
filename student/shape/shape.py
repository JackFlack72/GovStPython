import math


class Shape:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        return 0.0

    def __str__(self):
        return f"Shape: {self.name}"