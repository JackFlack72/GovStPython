# geometry_shape.py
# Interactive menu-driven turtle graphics program for drawing geometric shapes.

import turtle

# Menu Choice Constants
SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    # Mainline execution loop for shape selection and drawing
    choice = ""
    
    while choice != QUIT:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == SQUARE:
            x = float(input("Enter starting X coordinate: "))
            y = float(input("Enter starting Y coordinate: "))
            side = float(input("Enter side length: "))
            color = input("Enter fill color (e.g., red, blue, green): ").strip()
            square(x, y, side, color)
            
        elif choice == CIRCLE:
            x = float(input("Enter starting X coordinate: "))
            y = float(input("Enter starting Y coordinate: "))
            radius = float(input("Enter radius: "))
            color = input("Enter fill color (e.g., red, blue, green): ").strip()
            circle(x, y, radius, color)
            
        elif choice == TRIANGLE:
            x = float(input("Enter starting X coordinate: "))
            y = float(input("Enter starting Y coordinate: "))
            side = float(input("Enter side length: "))
            color = input("Enter fill color (e.g., red, blue, green): ").strip()
            equilateral_triangle(x, y, side, color)
            
        elif choice == QUIT:
            print("\nExiting program. Goodbye!")
            
        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")

    turtle.done()


def display_menu():
    # Displays user menu options
    print("\nShape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


def square(x, y, side, color):
    # Draws a filled square at coordinate (x, y)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()


def equilateral_triangle(x, y, side, color):
    # Draws a filled equilateral triangle at coordinate (x, y)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()


def circle(x, y, radius, color):
    # Draws a filled circle centered relative to starting position (x, y)
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


if __name__ == "__main__":
    main()