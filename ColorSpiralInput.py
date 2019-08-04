# ColorSpiralInput.py
# Billy Ridgeway
# Creates a colorful spiral with the number of sides input by the user.

import turtle               # Imports turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the pen speed to fast.
turtle.bgcolor("black")     # Sets the background color to black.

# Set up a list of any 8 valid Python color names.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]

# Ask the user for the number of sides. Default is 4, minimum is 1 and maximum is 8.
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))

# Draw a colorful spiral with the user specified number of sides.
for x in range (360):                   # Sets the value of 'x' to 360.
    t.pencolor( colors[x % sides] )     # Cycles through the pen colors based on the number
                                        # of sides selected by the user.
    t.forward( x * 3 / sides + x )      # Moves the pen forward the value of 'x' times 3
                                        # divided by the number of sides plus 'x'.
    t.left(360/sides + 1)               # Move the pen left by 360 divided by the number
                                        # of sides plus 1.
    t.width( x * sides / 200)           # Set the pen's width to the value of 'x' times
                                        # the number of sides divided by 200.
   
