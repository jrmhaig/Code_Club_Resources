    for event in pygame.event.get():
        ...
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed
            ...                               # New (next 4 lines)
            elif event.key == pygame.K_SPACE and bullet == None:
                # Fire the bullet from the mid-point of the ship
                bullet = GamePiece(ship.x+22, ship.y, bullet_image)
                bullet.direction = UP
    ...

    # Put the ship on the screen
    ship.draw()

    # Move and draw the bullet                     # New
    if bullet != None:                             # New
        bullet.move()                              # New
        if bullet.y > bullet.min_y:                # New
            bullet.draw()                          # New
        else:                                      # New
            bullet = None                          # New
