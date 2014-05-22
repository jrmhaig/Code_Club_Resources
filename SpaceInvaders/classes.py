import pygame

# Colours
WHITE = (255,255,255)

# Size of the screen
WIDTH = 400
HEIGHT = 300

pygame.init()
clock = pygame.time.Clock()
game_speed=85
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0)

class GamePiece:                                            # New
    def __init__(self, x, y, image):                        # New
        self.x = x                                          # New
        self.y = y                                          # New
        self.speed = 1                                      # New
        self.image = image                                  # New
        self.move_left = False                              # New
        self.move_right = False                             # New
        self.min_x = 10                                     # New
        self.max_x = 340                                    # New

    def move(self):                                         # New
        if self.move_left:                                  # New
            if self.x > self.min_x:                         # New
                self.x = self.x - self.speed                # New
        if self.move_right:                                 # New
            if  self.x < self.max_x:                        # New
                self.x = self.x + self.speed                # New

    def draw(self):                                         # New
        screen.blit(self.image, (self.x, self.y))           # New

# Images
ship_image = pygame.image.load('ship.png')

# Game objects                                              # Changed
ship = GamePiece(150, 260, ship_image)                      # Changed

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
                ship.move_left = True                       # Changed
            elif event.key == pygame.K_RIGHT:
                # Start moving the ship right
                ship.move_right = True                      # Changed
        elif event.type == pygame.KEYUP:
            # A key has been released
            if event.key == pygame.K_LEFT:
                # Stop moving the ship left
                ship.move_left = False                      # Changed
            elif event.key == pygame.K_RIGHT:
                # Stop moving the ship right
                ship.move_right = False                     # Changed

    ship.move()                                             # Changed

    # Put the ship on the screen
    ship.draw()                                             # Changed

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
