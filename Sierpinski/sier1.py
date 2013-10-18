from turtle import *

# Get the current position
#
# New commands:
#   turtle.position()
#   str(number)

x, y = position()

print("x position is " + str(x))
print("y position is " + str(y))

forward(100)

print("Drawing line ...")
x, y = position()

print("x position is " + str(x))
print("y position is " + str(y))
