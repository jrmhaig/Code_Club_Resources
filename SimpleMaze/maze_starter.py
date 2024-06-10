import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor('red_character', pos=(100, 100))

def draw():
    screen.clear()
    player.draw()
    
def move(sprite, x, y):
    sprite.x += x
    sprite.y += y
    if not 0 < sprite.x < WIDTH or not 0 < sprite.y < HEIGHT:
        sprite.x -= x
        sprite.y -= y

def update():
    if keyboard[keys.RIGHT]:
        move(player, 5, 0)
    if keyboard[keys.LEFT]:
        move(player, -5, 0)
    if keyboard[keys.DOWN]:
        move(player, 0, 5)
    if keyboard[keys.UP]:
        move(player, 0, -5)

pgzrun.go()
