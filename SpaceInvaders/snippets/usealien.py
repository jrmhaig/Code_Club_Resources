...
    # Put the ship on the screen
    ship.draw()

    # Move and draw the alien       # New
    alien.move()                    # New
    alien.draw()                    # New

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
