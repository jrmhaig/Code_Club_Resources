    # Move and draw the bullet
    if bullet != None:
        bullet.move()
        if bullet.y > bullet.min_y:
            bullet.draw()
            for alien in aliens:
                if alien.detect_hit(bullet):
                    aliens.remove(alien)
                    bullet = None
                    score = score + 10                        # New
                    break
        else:
            bullet = None

    score_text = font.render("Score: " + str(score), 1, BLUE) # New
    screen.blit(score_text, (10, 10))                         # New
