    for event in pygame.event.get():
        ...
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed
            ...
            elif event.key == pygame.K_SPACE and bullet == None:        # New
                # Fire the bullet from the mid-point of the ship        # New
                bullet = GamePiece(ship.x + 22, ship.y, bullet_image)   # New
                bullet.move_up = True                                   # New
    ...

    # Put the ship on the screen
    ship.draw()
    alien.draw()

    # Move and draw the bullet                                          # New
    if bullet != None:                                                  # New
        bullet.move()                                                   # New
        if bullet.x > bullet.min_x:                                     # New
            bullet.draw()                                               # New
        else:                                                           # New
            bullet = None                                               # New
