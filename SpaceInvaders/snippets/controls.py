import pygame

# Colours
WHITE = (255,255,255)

# Size of the screen
WIDTH = 400
HEIGHT = 300

pygame.init()
clock = pygame.time.Clock()
game_speed = 85
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0)

# Images                                                # New
ship_image = pygame.image.load('icons/ship.png')        # New

# Position of the ship                                  # New
ship = {                                                # New
        'x': 150,                                       # New
        'y': 260,                                       # New
        }                                               # New

run = True

while run:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:              # New
            # A key has been pressed                    # New
            if event.key == pygame.K_LEFT:              # New
                # Move the ship left                    # New
                ship['x'] = ship['x'] - 1               # New
            elif event.key == pygame.K_RIGHT:           # New
                # Move the ship right                   # New
                ship['x'] = ship['x'] + 1               # New

    # Put the ship on the screen                        # New
    screen.blit(ship_image, (ship['x'], ship['y']))     # New

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
