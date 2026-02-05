import turtle
import pygame # Added pygame for playing sound

# Initialize the pygame mixer for sound
pygame.mixer.init()

my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
y_coordinate = -125

def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(border_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.circle(radius)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(text_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.write("Happy", font=("sans-serif", 26, "bold"))
    my_turtle_cursor.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(text_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.write("Birthday", font=("sans-serif", 26, "bold"))
    my_turtle_cursor.getscreen().update()

def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(200)
    my_turtle_cursor.end_fill()

def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Set background color of the screen
my_turtle_screen.bgcolor("pink")

# Define parts of the cake
parts_of_cake = []
parts_of_cake.append(["#FF69B4", "#000000", 3, 30])  # Hot Pink
parts_of_cake.append(["#FFB6C1", "#000000", 3, 20])  # Light Pink
parts_of_cake.append(["#FF1493", "#000000", 3, 60])  # Deep Pink

# Draw cake layers
draw_layer_of_the_cake("#FFB6C1", "#000000", 3, -220, y_coordinate - 70, 400, 10)

for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]

# Draw cake toppings
draw_toppings_on_cake("#32CD32", "#000000", -120, y_coordinate - 60, 10)  # Lime Green
draw_toppings_on_cake("#FF69B4", "#000000", -80, y_coordinate - 60, 10)   # Hot Pink
draw_toppings_on_cake("#FFFF00", "#000000", 25, y_coordinate - 60, 10)    # Yellow
draw_toppings_on_cake("#1E90FF", "#000000", 59, y_coordinate - 60, 10)    # Dodger Blue
draw_toppings_on_cake("#2F4F4F", "#000000", -80, y_coordinate - 80, 10)   # Dark Slate Gray
draw_toppings_on_cake("#00BFFF", "#000000", -65, y_coordinate - 110, 10)  # Deep Sky Blue
draw_toppings_on_cake("#FFD700", "#000000", -95, y_coordinate - 140, 10)  # Gold
draw_toppings_on_cake("#2F4F4F", "#000000", 10, y_coordinate - 80, 10)    # Dark Slate Gray
draw_toppings_on_cake("#D3D3D3", "#000000", -20, y_coordinate - 110, 10)  # Light Gray
draw_toppings_on_cake("#8B0000", "#000000", 35, y_coordinate - 140, 10)   # Dark Red
draw_candle_for_cake("#FF1493", "#000000", -40, y_coordinate - 60)        # Deep Pink Candle

# Draw the stick for the candle
draw_stick_on_candle("#2F4F4F", -26, y_coordinate + 15, 7)  # Dark Slate Gray Stick
draw_stick("#2F4F4F", "#2F4F4F", 0, y_coordinate - 60)  # Dark Slate Gray Stick
draw_circle_on_top_of_stick("#FFD700", "#FFF5EE", 100, y_coordinate + 235, 100)  # Gold circle with light background

# Write text inside the circles
write_happy_inside_circle("#000000", -70, y_coordinate + 240)  # Black text
write_birthday_inside_circle("#FF1493", -80, y_coordinate + 190)  # Deep Pink text

# Play the sound after drawing is done
pygame.mixer.music.load("song/Birthday Melody.mp3")
pygame.mixer.music.play()

# Keep the Turtle window open
turtle.done()
