...

bullet = None
ship = GamePiece(150, 260, ship_image)
aliens = []                                         # Changed
for i in range(5):                                  # New
    alien = GamePiece(30 + i*50, 30, alien_image)   # New
    # Keep aliens in line when they bounce          # New
    alien.min_x = 20 + i*50                         # New
    alien.max_x = 140 + i*50                        # New
    # Make the alien move by itself                 # Changed
    alien.move_left = True                          # Changed
    # Make the alien bounce when it hits the edge   # Changed
    alien.bounce = True                             # Changed
    alien.speed = 0.3                               # Changed
    # Set the height and width of the alien         # Changed
    alien.width = 47                                # Changed
    alien.height = 22                               # Changed
    aliens.append(alien)                            # New

run = True

...
