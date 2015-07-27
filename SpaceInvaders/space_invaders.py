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

ALIEN_ROW_LENGTH = 10
ALIEN_TOP = ( 5 * HEIGHT ) / 100
ALIEN_ROW_LEFT = (5 * WIDTH) / 100
ALIEN_ROW_RIGHT = (95 * WIDTH) / 100
ALIEN_SPACE = ( 7 * WIDTH ) / 100
aliens = []
for i in range(ALIEN_ROW_LENGTH):
    aliens.append(Alien('alien1',
        ( ALIEN_ROW_LEFT + ALIEN_SPACE * i, ALIEN_TOP ),
        ALIEN_ROW_LEFT, ALIEN_ROW_RIGHT))

#alien1 = Alien('alien1', (100, 100), 100, 500)

def draw():
    screen.clear()
    ship.draw()
    for alien in aliens:
        alien.draw()

def update():
    if keyboard.LEFT and ship.x > ship.x_min:
        ship.x -= ship.speed
    if keyboard.RIGHT and ship.x < ship.x_max:
        ship.x += ship.speed
    for alien in aliens:
        alien.move()
