import turtle

# Setup
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.color("purple")

# Draw the petals
for i in range(36):
    t.circle(100, 60)   # Draw a 60-degree arc
    t.left(120)         # Turn to create the point of the petal
    t.circle(100, 60)   # Draw the other side of the petal
    t.left(10)          # Shift slightly to start the next petal

# Draw the stem
t.color("green")
t.setheading(270)       # Point the turtle down
t.forward(200)

turtle.done()