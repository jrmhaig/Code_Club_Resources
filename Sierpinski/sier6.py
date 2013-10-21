from turtle import *
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

    dist = distance( point[0], point[1] )

    #print("Distance from turtle to point: " + str(dist))

    #print("Drawing line of half that distance ...")

    forward(dist/2)

    dot(2)
