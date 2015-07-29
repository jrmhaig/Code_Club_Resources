from random import randrange
import time

# Size of the screen
WIDTH = 800
HEIGHT = 600

def x_percent(x):
    """ Find x position or length as a percentage of the screen width """
    return (x * WIDTH) / 100

def y_percent(y):
    """ Find y position or length as a percentage of the screen height """
    return (y * HEIGHT) / 100

# Data on the aliens
ALIEN_DATA = [
    { 'image': 'alien1', 'bullet': 'alien1-bullet' },
    { 'image': 'alien2', 'bullet': 'alien2-bullet', 'shoot_chance': 1, 'score': 30 },
    { 'image': 'alien3', 'bullet': 'alien3-bullet', 'shoot_chance': 1, 'score': 20 },
    { 'image': 'alien4', 'bullet': 'alien4-bullet', 'shoot_chance': 1, 'score': 10 }]
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
# Maximum number of alien bullets
MAX_ALIEN_BULLETS = 10

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
        self.data = ALIEN_DATA[alien_type]
        self.score = ALIEN_DATA[alien_type]['score']

    def move(self):
        self.x += self.h_speed
        if self.x >= self.x_max or self.x <= self.x_min:
            self.h_speed = -self.h_speed
            self.y -= self.v_speed
        if state['ship'] and len(state['alien_bullets']) < MAX_ALIEN_BULLETS and randrange(10000) < self.data['shoot_chance']:
            state['alien_bullets'].append(Bullet(BULLET_SPEED, self.data['bullet'], (self.x, self.y)))

state = {
    'score': 0,
    'next_ship_start': time.time(),
    'lives': [
        Actor('ship', (x_percent(50), y_percent(85))),
        Actor('ship', (x_percent(10), y_percent(95))),
        Actor('ship', (x_percent(5), y_percent(95)))
    ],
    'ship': None,
    'bullets': [],
    'aliens': [],
    'alien_bullets': []
}

for n, t in enumerate(ALIEN_ROWS):
  for i in range(ALIEN_ROW_LENGTH):
      state['aliens'].append(
          Alien(
              t,
              (
                  ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
                  ALIEN_TOP + ALIEN_V_SPACE * n),
              ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
              ALIEN_ROW_RIGHT - ALIEN_H_SPACE * (ALIEN_ROW_LENGTH - (i + 1))))

def draw():
    screen.clear()
    for s in state['lives']:
        s.draw()

    # Aliens
    for alien in state['aliens']:
        alien.draw()

    # Bullets
    for bullet in state['bullets']:
        bullet.draw()
    for bullet in state['alien_bullets']:
        bullet.draw()

    screen.draw.text("Score: %d" % state['score'], (SCORE_POS))

def next_ship():
    """ Get the next ship """
    state['ship'] = state['lives'][0]
    state['ship'].speed = 5
    state['ship'].x = x_percent(50)
    state['ship'].y = y_percent(88)
    state['ship'].x_min = x_percent(5)
    state['ship'].x_max = x_percent(95)

def update():
    if state['ship']:
        if keyboard.LEFT and state['ship'].x > state['ship'].x_min:
            state['ship'].x -= state['ship'].speed
        if keyboard.RIGHT and state['ship'].x < state['ship'].x_max:
            state['ship'].x += state['ship'].speed
    elif time.time() > state['next_ship_start']:
        next_ship()

    aliens_to_remove = []
    bullets_to_remove = []
    alien_bullets_to_remove = []

    # Move the aliens and detect if they have been hit
    for a, alien in enumerate(state['aliens']):
        alien.move()
        for b, bullet in enumerate(state['bullets']):
            if alien.colliderect(bullet):
                state['score'] += alien.score
                aliens_to_remove.append(a)
                bullets_to_remove.append(b)
    # Move the bullets fired by the player
    for i, bullet in enumerate(state['bullets']):
        bullet.move()
        if bullet.y < 0:
            bullets_to_remove.append(i)

    # Move the bullets fired by the aliens
    for i, bullet in enumerate(state['alien_bullets']):
        bullet.move()
        if state['ship'] and bullet.colliderect(state['ship']):
            sounds.explosion.play()
            state['ship'] = None
            del state['lives'][0]
            state['next_ship_start'] = time.time() + 3
            if len(state['lives']) == 0:
                # Game over
                exit()
        if bullet.y > HEIGHT:
            alien_bullets_to_remove.append(i)

    # Remove dead aliens and bullets
    for i in reversed(aliens_to_remove):
        del state['aliens'][i]
    for i in reversed(bullets_to_remove):
        del state['bullets'][i]
    for i in reversed(alien_bullets_to_remove):
        del state['alien_bullets'][i]

def on_key_down(key):
    if state['ship'] and key == keys.SPACE and len(state['bullets']) < MAX_BULLETS:
        sounds.shoot.play()
        state['bullets'].append(Bullet(-BULLET_SPEED, 'bullet', (state['ship'].x, state['ship'].y)))
