import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("2048 Game Board")
screen.bgcolor("blue")
screen.setup(width=680, height=595)

# Initialize turtle for drawing the board
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()
drawer.hideturtle()

# Define colors for each tile value
colors = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

# Board layout with values
board = [
    [2, None, 8, 8],
    [4, 4, None, 64],
    [128,None,16, 64],
    [2, 1024, 512, 2048]
]

# Size of each tile
tile_size = 90

# Function to draw a single tile
def draw_tile(x, y, value):
    drawer.goto(x, y)
    drawer.color("black", colors.get(value,"#cdc1b4"))  # Default color for empty tiles.

    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(tile_size)
        drawer.right(90)
    drawer.end_fill()

    # Draw number if there is a value
    if value:
        drawer.goto(x + tile_size / 2, y - tile_size / 2)
        drawer.color("black" if value <= 4 else "white")
        drawer.write(value, align="center", font=("Arial", 24, "bold"))

# Function to draw the entire board
def draw_board():
    y_start = 100  # Starting y-coordinate
    for row in board:
        x_start = -150  # Starting x-coordinate
        for value in row:
            draw_tile(x_start, y_start, value)
            x_start += tile_size + 10  # Move right for next tile
        y_start -= tile_size + 10  # Move down for next row

# Function to display score and high score
def draw_scores():
    # Score
    drawer.goto(-215, 180)
    drawer.color("white")
    drawer.write("Score: 3033", align="left", font=("Arial", 18, "bold"))

    # High Score
    drawer.goto(50, 180)
    drawer.color("white")
    drawer.write("High Score: 3032", align="left", font=("Arial",20, "bold"))

# Function to draw symbols (home, back, reset)
def draw_symbols():
    # Home symbol
    drawer.goto(-250, 240)
    drawer.color("white")
    drawer.write("🏠", align="center", font=("Arial", 20, "bold"))

    # Back symbol
    drawer.goto(-150, 240)
    drawer.color("white")
    drawer.write("↩", align="center", font=("Arial", 20, "bold"))

    # Reset symbol
    drawer.goto(200, 240)
    drawer.color("white")
    drawer.write("🔄", align="center", font=("Arial", 20, "bold"))

# Draw the 2048 game board and additional UI elements
draw_board()
draw_scores()
draw_symbols()

turtle.done()
