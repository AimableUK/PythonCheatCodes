import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(10)
screen = turtle.Screen()
screen.bgcolor("white")

def draw_house(x, y, width, height, door_width, roof_height):
    # Move to starting position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw the house (rectangle)
    t.begin_fill()
    t.fillcolor("white")
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    # Draw the roof (triangle)
    t.begin_fill()
    t.fillcolor("brown")
    t.goto(x, y + height)  # Move to top-left corner of the house
    t.goto(x + width / 2, y + height + roof_height)  # Top of the roof
    t.goto(x + width, y + height)  # Top-right corner of the house
    t.goto(x, y + height)  # Back to top-left corner of the house
    t.end_fill()

    # Draw the door (rectangle)
    door_height = height / 3
    door_x = x + (width - door_width) / 2
    t.penup()
    t.goto(door_x, y)
    t.pendown()
    
    t.begin_fill()
    t.fillcolor("green")
    for _ in range(2):
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
    t.end_fill()

    # Draw the windows (two squares)
    window_size = width / 5
    window_gap = width / 10
    
    t.penup()
    t.goto(x + window_gap, y + height * 2 / 3)
    t.pendown()
    t.begin_fill()
    t.fillcolor("lightblue")
    for _ in range(4):
        t.forward(window_size)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x + width - window_gap - window_size, y + height * 2 / 3)
    t.pendown()
    t.begin_fill()
    t.fillcolor("lightblue")
    for _ in range(4):
        t.forward(window_size)
        t.left(90)
    t.end_fill()

# Draw multiple houses
draw_house(-200, -100, 100, 120, 30, 60)
draw_house(-50, -100, 70, 80, 25, 40)
draw_house(60, -100, 50, 60, 20, 30)
draw_house(140, -100, 120, 150, 40, 70)
draw_house(300, -100, 40, 50, 15, 25)

# Hide turtle and finish
t.hideturtle()
turtle.done()
