from turtle import *
from math import sqrt

# Draw towards a point
# New commands:
#   math.sqrt(number)
#
# New syntax:
#   Mathematical operations ** and /

point = [ 100, 100 ]

angle = towards(point[0], point[1])
print("Angle to point is " + str(angle) + " degrees")

print("Turning towards that point ...")

setheading(angle)

x, y = position()
print("Current x = " + str(x))
print("Current y = " + str(y))

# Year 6 kids may or may not have heard of Pythagoras
distance = sqrt( (point[0] - x)**2 + (point[1] - y)**2 )

print("Distance from turtle to point: " + str(distance))

print("Drawing line of half that distance ...")

forward(distance/2)
