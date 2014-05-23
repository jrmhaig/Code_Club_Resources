...

    # Move and draw the ship
    ship.move()
    ship.draw()

    # Move and draw the aliens                          # Changed
    for alien in aliens:                                # Changed
        alien.move()                                    # Changed
        alien.draw()                                    # Changed

    # Move and draw the bullet
    if bullet != None:
        bullet.move()
        if bullet.y > bullet.min_y:
            bullet.draw()
            for alien in aliens:                        # Changed
                if alien.detect_hit(bullet):            # Changed
                    aliens.remove(alien)                # Changed
                    bullet = None                       # Changed
                    break                               # Changed
        else:
            bullet = None

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
