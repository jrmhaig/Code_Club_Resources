# Simple Maze

In this project you will create a simple maze game. The maze will be made up of
rectangular blocks around the screen.

This project will introduce:

* The PyGame `Rect` object
* Detecting collision between one sprite (the player) and a list of other
  sprites (the walls)

## Starter

Here is the code to get started:

```python
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
```

Try to understand what it is doing before reading the explanation below.

### Explanation of the starter code

1. A sprite is created called `player` from the image file `red_character.png`
   and it is put at the coordinates (100, 100) to start.
2. The `draw` function clears the screen and draws the `player` sprite.
3. The `update` function detects when each of the four direction keys are
   pressed and then uses the `move` method to move the `player` sprite.
4. The `move` function takes three arguments; `sprite`, `x` and `y`. It then
   tried to move `sprite` by `x` steps right and `y` steps down. If `x` or `y`
   are negative then the sprite will move left or up instead. If the movement
   puts the sprite off the screen then its position is put back by subtracting
   `x` and `y`.

## Adding a wall

The walls of the maze are going to be made up of rectangular blocks. These can
be created using `Rect`. Near the top of your code:

```python
# After this line
player = Actor('red_character', pos=(100, 100))

# Add this line
wall = Rect((200, 200), (100, 100))
PURPLE = (150, 50, 255)
```

Then in the `draw` method add:

```python
    screen.draw.filled_rect(wall, PURPLE)
```

Run your code and check that a red box has appeared.

`Rect` defines a rectangular box with two *tuples*; the first, `(200, 200)`, is
the top-left point of the rectangle and the second, `(100, 100)`, is the width
and height. Try changing these numbers to see what happens to the box.

> [!NOTE]
> A *tuple* are used to store multiple values in a single variable. Tuples are
> used here three times;
> * The top-left point of the rectangle is the tuple `(200, 200)`.
> * The size of the rectangle is represented by the tuple `(100, 100)`.
> * The colour is defined as a tuple containing the red, green and blue
>   components. In this case it is 150 red, 50 green and 255 blue. Try
>   different numbers, which must be between 0 and 255.

## Make the walls solid

At the moment you can run through the wall so we need to stop the `player` when
it touches it. The `move` function already stops the `player` running off the
edge so we can simply add something to check if is hitting the wall. First we
can do it for a single wall and later we will change it to have many walls.

The `player` has a function called `colliderect` that is `True` if it is
touching another object or `False` if it is not. Find this line in the `move`
function:

```python
    if not 0 < sprite.x < WIDTH or not 0 < sprite.y < HEIGHT:
```

and change it to this:

```python
    if not 0 < sprite.x < WIDTH or not 0 < sprite.y < HEIGHT or player.colliderect(wall):
```

That's it! Try it now and you should see that the player cannot go through the
wall any more.

## More walls

One wall doesn't make much of a maze. You could create lots of walls and then
test them like this:

```python
    player.colliderect(wall1) or player.colliderect(wall2) or ...
```

Fortunately, there is a better way. Instead of `colliderect` we can use
`collidelist`, which checks if the sprite is touching any of a list of other
sprites.

At the top of your code you will need to change how you make your wall;

```python
# Change this line
wall = Rect((200, 200), (100, 100))

# To this
walls = [
    Rect((200, 200), (100, 100)),
    Rect((400, 200), (50, 10)),
    Rect((100, 500), (600, 100))
]
```

So instead of a single wall made up of one rectangle we have a list made up of
three.

> [!NOTE]
> A *list* is also called an *array.*

Now that we have a list of walls instead of a single wall the code to draw them
has to change. In the `draw` method make the following change:

```python
    # Change
    screen.draw.filled_rect(wall, PURPLE)

    # To this
    for wall in walls:
        screen.draw.filled_rect(wall, PURPLE)
```

Then finally we need to change the code to check the collision to use
`collidelist` instead of `colliderect`. In the `move` method:

```python
# In the 'if' statement, change
player.colliderect(wall)

# To this
player.collidelist(walls) > -1
```

> [!NOTE]
> `colliderect` returns either `True` or `False` but `collidelist` returns a
> number to show which object the player is touching or -1 if it is not touching
> any.
