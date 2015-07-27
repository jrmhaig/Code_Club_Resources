# Size of the screen
WIDTH = 800
HEIGHT = 600

def x_percent(x):
    return (x * WIDTH) / 100

def y_percent(y):
    return (y * HEIGHT) / 100

# Data on the aliens
ALIEN_DATA = [
    { 'image': 'alien1', 'bullet': 'alien1-bullet' },
    { 'image': 'alien2', 'bullet': 'alien2-bullet', 'score': 30 },
    { 'image': 'alien3', 'bullet': 'alien3-bullet', 'score': 20 },
    { 'image': 'alien4', 'bullet': 'alien4-bullet', 'score': 10 }]
# Number of aliens in a row
ALIEN_ROW_LENGTH = 10
# Alien types in each row (top to bottom)
ALIEN_ROWS = [ 1, 2, 2, 3, 3 ]
# Starting top position of the top row of aliens
ALIEN_TOP = y_percent(15)
# Furthest left position of the left most alien
ALIEN_ROW_LEFT = x_percent(5)
# Furthest right position of the right most alien
ALIEN_ROW_RIGHT = x_percent(95)
# Horizontal spacing of the aliens
ALIEN_H_SPACE = x_percent(7)
# Vertical spacing of the aliens
ALIEN_V_SPACE = y_percent(7)

# Position of the score
SCORE_POS = x_percent(2), y_percent(2)

# Speed of the bullets
BULLET_SPEED = 3
# Maximum number of bullets on the screen
MAX_BULLETS = 5

ship = Actor('ship', (x_percent(50), y_percent(95)))
ship.speed = 5
ship.x_min = x_percent(5)
ship.x_max = y_percent(95)

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
        self.score = ALIEN_DATA[alien_type]['score']

    def move(self):
        self.x += self.h_speed
        if self.x >= self.x_max or self.x <= self.x_min:
            self.h_speed = -self.h_speed
            self.y -= self.v_speed

aliens = []
for n, t in enumerate(ALIEN_ROWS):
  for i in range(ALIEN_ROW_LENGTH):
      aliens.append(
          Alien(
              t,
              (
                  ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
                  ALIEN_TOP + ALIEN_V_SPACE * n),
              ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
              ALIEN_ROW_RIGHT - ALIEN_H_SPACE * (ALIEN_ROW_LENGTH - (i + 1))))

bullets = []
ship.score = 0

def draw():
    screen.clear()
    ship.draw()

    # Aliens
    for alien in aliens:
        alien.draw()

    # Bullets
    for bullet in bullets:
        bullet.draw()

    screen.draw.text("Score: %d" % ship.score, (SCORE_POS))

def update():
    if keyboard.LEFT and ship.x > ship.x_min:
        ship.x -= ship.speed
    if keyboard.RIGHT and ship.x < ship.x_max:
        ship.x += ship.speed

    aliens_to_remove = []
    bullets_to_remove = []
    for a, alien in enumerate(aliens):
        alien.move()
        for b, bullet in enumerate(bullets):
            if alien.colliderect(bullet):
                ship.score += alien.score
                aliens_to_remove.append(a)
                bullets_to_remove.append(b)
    for i, bullet in enumerate(bullets):
        bullet.move()
        if bullet.y < 0:
            bullets_to_remove.append(i)

    for i in reversed(aliens_to_remove):
        del aliens[i]
    for i in reversed(bullets_to_remove):
        del bullets[i]

def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullets.append(Bullet(-BULLET_SPEED, 'bullet', (ship.x, ship.y)))
