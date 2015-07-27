WIDTH = 800
HEIGHT = 600

ship = Actor('ship', (WIDTH / 2, (95 * HEIGHT) / 100 ))
ship.speed = 5
ship.x_min = (5 * WIDTH) / 100
ship.x_max = (95 * WIDTH) / 100

class Alien(Actor):
    def __init__(self, image):
        super(image)

alien1 = Actor('ship')

def draw():
    screen.clear()
    ship.draw()
    alien1.draw()

def update():
    if keyboard.LEFT and ship.x > ship.x_min:
        ship.x -= ship.speed
    if keyboard.RIGHT and ship.x < ship.x_max:
        ship.x += ship.speed
