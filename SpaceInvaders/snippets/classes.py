import pygame

# Colours
WHITE = (255,255,255)

# Size of the screen
WIDTH = 400
HEIGHT = 300

# Directions                                            # New
LEFT = 1                                                # New
RIGHT = 2                                               # New
UP = 3                                                  # New
DOWN = 4                                                # New

pygame.init()
clock = pygame.time.Clock()
game_speed=85
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0)
pygame.key_set_repeat(1, 10)

class GamePiece:                                        # New
    def __init__(self, x, y, image):                    # New
        self.x = x                                      # New
        self.y = y                                      # New
        self.speed = 1                                  # New
        self.image = image                              # New
        self.min_x = 10                                 # New
        self.max_x = 340                                # New

    def move(self, direction):                          # New
        if direction == LEFT:                           # New
            if self.x > self.min_x:                     # New
                self.x = self.x - self.speed            # New
        elif direction == RIGHT:                        # New
            if  self.x < self.max_x:                    # New
                self.x = self.x + self.speed            # New

    def draw(self):                                     # New
        screen.blit(self.image, (self.x, self.y))       # New

# Images
ship_image = pygame.image.load('icons/ship.png')

# Game objects                                          # Changed
ship = GamePiece(150, 260, ship_image)                  # Changed

run = True

while run:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed
            if event.key == pygame.K_LEFT:
                # Start moving the ship left
                ship.move(LEFT)                         # Changed
            elif event.key == pygame.K_RIGHT:
                # Start moving the ship right
                ship.move(RIGHT)                        # Changed

    # Put the ship on the screen                        # Changed
    ship.draw()                                         # Changed

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
