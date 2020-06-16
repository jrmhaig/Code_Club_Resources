from turtle import *

# Turn towards a point
#
# New commands:
#   turtle.towards(x, y)
#   turtle.setheading(angle)
#
# New syntax:
#   array variables

point = ( 100, 100 )

angle = towards(point)
print("Angle to point is " + str(angle) + " degrees")

print("Turning towards that point ...")

setheading(angle)

print("Drawing line in that direction ...")

forward(100)
