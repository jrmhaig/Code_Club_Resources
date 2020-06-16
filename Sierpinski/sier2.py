from turtle import *

# Draw several dots towards the line
#
# New command:
#   dot(size)

penup()

point = ( 100, 100 )

for i in range(10):
    angle = towards(point)
    print("Angle to point is " + str(angle) + " degrees")

    print("Turning towards that point ...")

    setheading(angle)

    dist = distance(point)

    print("Distance from turtle to point: " + str(dist))

    print("Drawing line of half that distance ...")

    forward(dist/2)

    dot(5)
