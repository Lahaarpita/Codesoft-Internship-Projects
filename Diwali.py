import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Happy Diwali!")
screen.bgcolor("black")

# Create a turtle for writing text
pen = turtle.Turtle()
pen.color("yellow")
pen.hideturtle()
pen.speed(0)

# Function to write the initial greeting text
def write_text():
    pen.penup()
    pen.goto(0, 200)
    pen.write("Happy Diwali!", align="center", font=("Arial", 36, "bold"))

# Function to draw a rangoli pattern
def draw_rangoli():
    rangoli_turtle = turtle.Turtle()
    rangoli_turtle.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    rangoli_turtle.penup()
    rangoli_turtle.goto(0, 0)
    rangoli_turtle.pendown()

    for i in range(36):
        rangoli_turtle.color(colors[i % len(colors)])
        rangoli_turtle.circle(100)
        rangoli_turtle.right(10)

    rangoli_turtle.hideturtle()

# Function to draw fireworks
def draw_firework(x, y):
    firework = turtle.Turtle()
    firework.speed(0)
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]

    for _ in range(10):
        firework.color(random.choice(colors))
        firework.setheading(random.randint(0, 360))
        firework.forward(50)
        firework.backward(50)

    firework.hideturtle()

# Function to write the name at the end
def write_name():
    pen.penup()
    pen.goto(0, -250)
    pen.color("light blue")
    pen.write("Presented by:-Arpita Laha", align="center", font=("Arial", 24, "italic"))

# Function to show the final Diwali wish on a new page
def show_final_wish():
    screen.clearscreen()  # Clear the screen
    screen.bgcolor("dark violet")
    pen.color("gold")
    pen.penup()
    pen.goto(0, 0)
    pen.write("May the light of Diwali fill your life with joy and happiness!\nWishing you a prosperous and safe Diwali!",
              align="center", font=("Arial", 15,"bold"))

# Main program execution
write_text()
draw_rangoli()
write_name()  # Display name after the rangoli is drawn

# Firework display at random positions
for _ in range(5):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_firework(x, y)

# Wait for a moment, then show the final Diwali wish
time.sleep(2)
show_final_wish()

turtle.done()
