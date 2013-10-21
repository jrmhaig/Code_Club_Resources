from turtle import *
from random import randrange

# Choose a random start position

def randpoint():
    return [ randrange(401)-200, randrange(401)-200 ]

penup()

point = randpoint()

for i in range(10):
    angle = towards(point[0], point[1])
    print("Angle to point is " + str(angle) + " degrees")

    print("Turning towards that point ...")

    setheading(angle)

    dist = distance(point[0], point[1])

    print("Distance from turtle to point: " + str(dist))

    print("Drawing line of half that distance ...")

    forward(dist/2)

    dot(5)
