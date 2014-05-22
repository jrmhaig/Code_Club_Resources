...

# Position of the ship
ship = {
        'x': 150,
        'y': 260,
        }
ship_move_left = False                              # New
ship_move_right = False                             # New

run = True

while run:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed
            if event.key == pygame.K_LEFT:
                # Start moving the ship left        # Changed
                ship_move_left = True               # Changed
            elif event.key == pygame.K_RIGHT:
                # Start moving the ship right       # Changed
                ship_move_right = True              # Changed
        elif event.type == pygame.KEYUP:            # New
            # A key has been released               # New
            if event.key == pygame.K_LEFT:          # New
                # Stop moving the ship left         # New
                ship_move_left = False              # New
            elif event.key == pygame.K_RIGHT:       # New
                # Stop moving the ship right        # New
                ship_move_right = False             # New

    if ship_move_left:                              # New
        ship['x'] = ship['x'] - 1                   # New
    if ship_move_right:                             # New
        ship['x'] = ship['x'] + 1                   # New

    # Put the ship on the screen
    screen.blit(ship_image, (ship['x'], ship['y']))

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
