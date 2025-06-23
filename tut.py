import turtle
#1
t = turtle.Turtle()
t.speed(10)
t.color("green")
t.shape('arrow')
t.pensize(2)
for i in range(36):
    t.circle(100)
    t.right(10)

turtle.done()

#2
import turtle

t = turtle.Turtle()
t.speed(10)
t.color("green")
t.shape('arrow')
t.pensize(2)
for _ in range(6):
    t.forward(100)
    t.right(60)

turtle.done()

#3
import turtle

t = turtle.Turtle()
t.speed(10)
t.color("green")
t.shape('arrow')
t.pensize(2)
for i in range(100):
    t.forward(i * 5)
    t.right(144)

turtle.done()

#4
import turtle

t = turtle.Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

for i in range(6):
    t.color(colors[i])
    t.forward(100)
    t.right(60)

turtle.done()

#5
import turtle

t = turtle.Turtle()
t.pensize(3)
t.color('green')
t.speed(10)
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

for y in range(4):
    for x in range(4):
        t.penup()
        t.goto(x * 50, y * 50)
        t.pendown()
        draw_square(50)

turtle.done()

#6
import turtle

t = turtle.Turtle()
t.pensize(3)
t.color('green')
t.speed(10)
# User inputs the number of sides
sides = int(input("Enter the number of sides: "))
angle = 360 / sides

for _ in range(sides):
    t.forward(100)
    t.right(angle)

turtle.done()
#7
import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length*n)
    t.left(angle)

    draw(t, length, n-1)
    t.right(2*angle)
    draw(t, length, n-1)
    t.left(angle)
    t.backward(length*n)

bob = turtle.Turtle()
turtle.speed(11)  # Set turtle speed (optional)
bob.pensize(3)
bob.color('blue')

# Call the draw function
draw(bob, 10, 5)

# End the turtle graphics program
turtle.done()