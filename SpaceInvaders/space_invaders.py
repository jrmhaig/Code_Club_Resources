WIDTH = 800
HEIGHT = 600
ALIEN_DATA = [
    { 'image': 'alien1', 'bullet': 'alien1-bullet' },
    { 'image': 'alien2', 'bullet': 'alien2-bullet' },
    { 'image': 'alien3', 'bullet': 'alien3-bullet' },
    { 'image': 'alien4', 'bullet': 'alien4-bullet' }]
BULLET_SPEED = 3
MAX_BULLETS = 5

ship = Actor('ship', (WIDTH / 2, (95 * HEIGHT) / 100 ))
ship.speed = 5
ship.x_min = (5 * WIDTH) / 100
ship.x_max = (95 * WIDTH) / 100

class Bullet(Actor):
    def __init__(self, speed, *args, **kwargs):
        super(Bullet, self).__init__(*args, **kwargs)
        self.speed = speed

    def move(self):
        self.y += self.speed

class Alien(Actor):
    def __init__(self, alien_type, pos, x_min, x_max, anchor=('center', 'center')):
        super(Alien, self).__init__(ALIEN_DATA[alien_type]['image'], pos, anchor)
        self.x_min = x_min
        self.x_max = x_max
        self.h_speed = 1
        self.v_speed = -1

    def move(self):
        self.x += self.h_speed
        if self.x >= self.x_max or self.x <= self.x_min:
            self.h_speed = -self.h_speed
            self.y -= self.v_speed

ALIEN_ROW_LENGTH = 10
ALIEN_ROWS = 4
ALIEN_TOP = ( 5 * HEIGHT ) / 100
ALIEN_ROW_LEFT = (5 * WIDTH) / 100
ALIEN_ROW_RIGHT = (95 * WIDTH) / 100
ALIEN_H_SPACE = ( 7 * WIDTH ) / 100
ALIEN_V_SPACE = ( 7 * HEIGHT ) / 100
aliens = []
for n in range(ALIEN_ROWS):
  for i in range(ALIEN_ROW_LENGTH):
      aliens.append(
          Alien(
              n,
              (
                  ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
                  ALIEN_TOP + ALIEN_V_SPACE * n),
              ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
              ALIEN_ROW_RIGHT - ALIEN_H_SPACE * (ALIEN_ROW_LENGTH - (i + 1))))

bullets = []

def draw():
    screen.clear()
    ship.draw()

    # Aliens
    for alien in aliens:
        alien.draw()

    # Bullets
    to_remove = []
    for i, bullet in enumerate(bullets):
        bullet.draw()
        if bullet.y < 0:
            to_remove.append(i)
    for i in reversed(to_remove):
        del bullets[i]

def update():
    if keyboard.LEFT and ship.x > ship.x_min:
        ship.x -= ship.speed
    if keyboard.RIGHT and ship.x < ship.x_max:
        ship.x += ship.speed
    for alien in aliens:
        alien.move()
    for bullet in bullets:
        bullet.move()

def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullets.append(Bullet(-BULLET_SPEED, 'bullet', (ship.x, ship.y)))
