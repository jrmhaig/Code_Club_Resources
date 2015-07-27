WIDTH = 800
HEIGHT = 600

ship = Actor('ship', (WIDTH / 2, (95 * HEIGHT) / 100 ))
ship.speed = 5
ship.x_min = (5 * WIDTH) / 100
ship.x_max = (95 * WIDTH) / 100

class Alien(Actor):
    def __init__(self, image, pos, x_min, x_max, anchor=('center', 'center')):
        super(Alien, self).__init__(image, pos, anchor)
        self.x_min = x_min
        self.x_max = x_max
        self.speed = 1

    def move(self):
        self.x += self.speed
        if self.x >= self.x_max or self.x <= self.x_min:
            self.speed = -self.speed

alien1 = Alien('alien1', (100, 100), 100, 500)

def draw():
    screen.clear()
    ship.draw()
    alien1.draw()

def update():
    if keyboard.LEFT and ship.x > ship.x_min:
        ship.x -= ship.speed
    if keyboard.RIGHT and ship.x < ship.x_max:
        ship.x += ship.speed
    alien1.move()
