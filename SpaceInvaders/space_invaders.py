from random import randrange
import time

# Size of the screen
WIDTH = 800
HEIGHT = 600

BACKGROUND = (100, 100, 100)

def x_percent(x):
    """ Find x position or length as a percentage of the screen width """
    return (x * WIDTH) / 100

def y_percent(y):
    """ Find y position or length as a percentage of the screen height """
    return (y * HEIGHT) / 100

def chance(prob):
    return randrange(prob[1]) < prob[0]

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

        # 'Home' position of alien, when in formation
        self.home_x = self.x
        self.home_y = self.y
        self.diving = False
        self.diving_chance = [1, 10000]

        # Limits of alien's horizontal motion
        self.x_min = x_min
        self.x_max = x_max

        # Speed when in formation
        #   Horizontal - steps across per call to 'update'
        #   Vertial - steps down when changing direction
        self.h_speed = 1
        self.v_speed = 1

        self.data = ALIEN_DATA[alien_type]
        self.score = ALIEN_DATA[alien_type]['score']

    def move(self):
        # Keep track of home position
        self.home_x += self.h_speed
        if self.home_x >= self.x_max or self.home_x <= self.x_min:
            self.h_speed = -self.h_speed
            self.home_y += self.v_speed

        if self.diving:
            self.y += self.v_speed
            if game.ship:
                if self.x > game.ship.x:
                    self.x -= 1
                else:
                    self.x += 1
            if self.y > HEIGHT:
                self.diving = False
        else:
            # 'Special' actions only if the ship is in play
            if game.ship:
                # Fire bullets if;
                #       * There are not too many alien bullets
                #       * With probability determined by self.data['shoot_chance']
                if len(game.alien_bullets) < MAX_ALIEN_BULLETS and randrange(10000) < self.data['shoot_chance']:
                    game.alien_bullets.append(Bullet(BULLET_SPEED, self.data['bullet'], (self.x, self.y)))
                elif chance(self.diving_chance):
                    self.diving = True

            self.x = self.home_x
            self.y = self.home_y

class Game:
    """ Holds main game data """
    def __init__(self):
        self.reset() # Start the game with a fresh landscape and ship

    def reset(self):
        """ Start a new game """
        self.score = 0
        self.next_ship_start = time.time() # Time for the next ship to start
        self.lives = [
            Actor('ship', (x_percent(50), y_percent(85))),
            Actor('ship', (x_percent(10), y_percent(95))),
            Actor('ship', (x_percent(5), y_percent(95)))
        ] # Players lives
        self.ship = None # Current ship
        self.bullets = [] # Player's bullets on the screen
        self.aliens = [] # Aliens on the screen
        self.alien_bullets = [] # Aliens' bullets on the screen

        for n, t in enumerate(ALIEN_ROWS):
            for i in range(ALIEN_ROW_LENGTH):
                self.aliens.append(
                    Alien(
                        t,
                        (
                            ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
                            ALIEN_TOP + ALIEN_V_SPACE * n),
                        ALIEN_ROW_LEFT + ALIEN_H_SPACE * i,
                        ALIEN_ROW_RIGHT - ALIEN_H_SPACE * (ALIEN_ROW_LENGTH - (i + 1))))

game = Game()

def draw():
    screen.clear()
    screen.fill(BACKGROUND)

    for l in game.lives:
        l.draw()
    for a in game.aliens:
        a.draw()
    for ab in game.alien_bullets:
        ab.draw()
    for b in game.bullets:
        b.draw()

    screen.draw.text("Score: %d" % game.score, (SCORE_POS))

def next_ship():
    """ Get the next ship """
    game.ship = game.lives[0]
    game.ship.speed = 5
    game.ship.x = x_percent(50)
    game.ship.y = y_percent(88)
    game.ship.x_min = x_percent(5)
    game.ship.x_max = x_percent(95)

def update():
    if game.ship:
        if keyboard.LEFT and game.ship.x > game.ship.x_min:
            game.ship.x -= game.ship.speed
        if keyboard.RIGHT and game.ship.x < game.ship.x_max:
            game.ship.x += game.ship.speed
    elif time.time() > game.next_ship_start:
        next_ship()

    aliens_to_remove = []
    bullets_to_remove = []
    alien_bullets_to_remove = []

    # Move the aliens and detect if they have been hit
    for a, alien in enumerate(game.aliens):
        alien.move()
        if game.ship and alien.colliderect(game.ship):
            aliens_to_remove.append(a)
            sounds.explosion.play()
            game.ship = None
            del game.lives[0]
            game.next_ship_start = time.time() + 3
            if len(game.lives) == 0:
                # Game over
                exit()
        for b, bullet in enumerate(game.bullets):
            if alien.colliderect(bullet):
                game.score += alien.score
                aliens_to_remove.append(a)
                bullets_to_remove.append(b)
    # Move the bullets fired by the player
    for i, bullet in enumerate(game.bullets):
        bullet.move()
        if bullet.y < 0:
            bullets_to_remove.append(i)

    # Move the bullets fired by the aliens
    for i, bullet in enumerate(game.alien_bullets):
        bullet.move()
        if game.ship and bullet.colliderect(game.ship):
            sounds.explosion.play()
            game.ship = None
            del game.lives[0]
            game.next_ship_start = time.time() + 3
            if len(game.lives) == 0:
                # Game over
                exit()
        if bullet.y > HEIGHT:
            alien_bullets_to_remove.append(i)

    # Remove dead aliens and bullets
    for i in reversed(aliens_to_remove):
        del game.aliens[i]
    for i in sorted(bullets_to_remove, reverse=True):
        del game.bullets[i]
    for i in sorted(alien_bullets_to_remove, reverse=True):
        del game.alien_bullets[i]

def on_key_down(key):
    if game.ship and key == keys.SPACE and len(game.bullets) < MAX_BULLETS:
        sounds.shoot.play()
        game.bullets.append(Bullet(-BULLET_SPEED, 'bullet', (game.ship.x, game.ship.y)))
