from turtle import *
# from math import sqrt       # Only needed for Python 3
from random import randrange

# Draw Sierpinski's gasket!

# Note, comment (or remove) print statements or it will be slow

def randpoint():
    return [ randrange(401)-200, randrange(401)-200 ]

penup()
speed(11)

corners = [ randpoint(), randpoint(), randpoint() ]

for i in range(1000):
    n = randrange(3)
    point = corners[n]
    
    angle = towards(point[0], point[1])
    #print("Angle to point is " + str(angle) + " degrees")

    #print("Turning towards that point ...")

    setheading(angle)

    x, y = position()
    #print("Current x = " + str(x))
    #print("Current y = " + str(y))

    distance = sqrt( (point[0] - x)**2 + (point[1] -y)**2 )

    #print("Distance from turtle to point: " + str(distance))

    #print("Drawing line of half that distance ...")

    forward(distance/2)

    dot(2)
