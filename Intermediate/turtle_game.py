import turtle as t
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("lightblue")

# Create two turtles
turtle1 = turtle.Turtle()
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-200, 50)

turtle2 = turtle.Turtle()
turtle2.color("blue")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-200, -50)

# Start the race
def start_race():
    turtle1.pendown()
    turtle2.pendown()
    while True:
        turtle1.forward(random.randint(1, 10))  # Move turtle1 forward
        turtle2.forward(random.randint(1, 10))  # Move turtle2 forward
        
        # Check for a winner
        if turtle1.xcor() >= 200:
            print("Red Turtle Wins!")
            break
        elif turtle2.xcor() >= 200:
            print("Blue Turtle Wins!")
            break

# Button to start the race
start_button = turtle.Turtle()
start_button.hideturtle()
start_button.penup()
start_button.goto(0, 200)
start_button.write("Press 'Enter' to Start the Race", align="center", font=("Arial", 16, "normal"))

# Function to start the race when 'Enter' is pressed
def on_enter():
    start_button.clear()  # Clear the start message
    start_race()

# Listen for key press
screen.listen()
screen.onkey(on_enter, "Return")

# Keep the window open
turtle.mainloop()
