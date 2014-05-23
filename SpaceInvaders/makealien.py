...

# Images
ship_image = pygame.image.load('icons/ship.png')
alien_image = pygame.image.load('icons/alien1.png')      # New

ship = GamePiece(150, 260, ship_image)
alien = GamePiece(150, 30, alien_image)                 # New

# Make the alien move by itself                         # New
alien.move_left = True                                  # New
# Make the alien bounce when it hits the edge           # New
alien.bounce = True                                     # New
alien.speed = 0.3                                       # New

...
