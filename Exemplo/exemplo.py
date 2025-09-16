import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set pen color and fill color
my_turtle.color("red", "yellow")

# Begin filling the shape
my_turtle.begin_fill()

# Draw a star
while True:
    my_turtle.forward(200)
    my_turtle.left(170)
    if abs(my_turtle.pos()) < 1:
        break

# End filling the shape
my_turtle.end_fill()

# Keep the window open until closed manually
turtle.done()