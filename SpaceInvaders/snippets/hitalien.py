    # Move and draw the bullet
    if bullet != None:
        bullet.move()
        if bullet.y > bullet.min_y:
            bullet.draw()
            if alien.detect_hit(bullet):                # New
                # Move the alien back to the top        # New
                alien.x = 150                           # New
                alien.y = 30                            # New
                # Move it a bit faster                  # New
                alien.speed = alien.speed + 0.1         # New
                bullet = None                           # New
        else:
            bullet = None
