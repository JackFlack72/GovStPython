from shape.rectangle import Rectangle
from shape.circle import Circle


def main():
    # List of mixed shape objects processed polymorphically
    shapes = [
        Rectangle("rect1", 4, 5),
        Circle("circle1", 3),
        Rectangle("rect2", 4, 4),
        Circle("circle2", 1.5),
    ]

    print("Areas of various shapes:")
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.get_area():.2f}")


if __name__ == "__main__":
    main()