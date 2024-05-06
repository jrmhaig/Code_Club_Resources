# Catch the Gems

This is part two of an introduction to [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) and it will introduce:

* Controlling the player sprite with the keyboard
* Making random choices
* Detecting collision between sprites
* Playing sound

## The Player's Sprite

Add the following code to create the window and add a new sprite for the
player to control.

```python
import pgzrun
from random import randrange

WIDTH = 800
HEIGHT = 500

player = Actor('green_character.png')
player.x = randrange(0, WIDTH)
player.y = randrange(0, HEIGHT)

def draw():
    screen.clear()
    player.draw()

pgzrun.go()
```

There are four characters you can choose: `green_character`, `purple_character`,
`red_character` or `yellow_character`. Choose your favourite.

This time the `x` and `y` position of the sprite is chosen randomly using the
`randrange` (random number from a range) function. It takes two arguments for
the minumum and maximum value in the range. In this case, the `x` position is
between 0, the very left-hand side, and `WIDTH`, which is the very right-hand
side. By using `WIDTH` instead of `800` we make sure that it will still work if
`WIDTH` and `HEIGHT` are changed.

In this code `x` and `y` are set separately but they can be set in one line with
`pos`:

```python
player.x = randrange(0, WIDTH)
player.y = randrange(0, HEIGHT)

# is exactly the same as

player.pos = (randrange(0, WIDTH), randrange(0, HEIGHT))
```

You can use whichever version you want.

> [!NOTE]
> The `randrange` function comes from the `random` library and we can use it
> because of the `from random import randrange` at the top. This is similar to
> the `import pyzrun` line above. The difference is that the whole of the
> `pyzrun` library is added but only the single `randrange` function is added
> from the `random` library. Later on another function will be added from
> `random`.

## Controlling the player

The `update` function allows attributes of all the sprites to be updated 60
times every second. The following code will check to see if the right arrow key
is pressed and, if it is, move the player a little to the right:

```python
def update():
    if keyboard[keys.RIGHT]:
        player.x += 5
```

The `player.x += 5` takes the `x` position of the player sprite and adds 5 to
it. You may also have seen something like this, which is the same;

```python
player.x = player.x + 5
```

Again, you can use whichever version you prefer.

Now add extra code so that you can also move left, up and down.

## Stop the player going too far

You may have noticed that you can run the player off the screen. This is
different from Scratch, where the sprites cannot escape the stage. We will need
to add a check to stop the player going too far. In your `update` function make
the following change:

```python
    if keyboard[keys.RIGHT]:
        player.x += 5
        # Add these lines
        if player.x > WIDTH:
            player.x -= 5
```

These extra two lines check if the player's sprite has gone off the right of the
screen and, if so, moves it back on. The same needs to be done for each of the
other keys. What should go in place of `player.x > WIDTH` in each case?

## Add a gem to collect

There are four gem image files to use; `gem_blue`, `gem_yellow`, `gem_green.png`
and `gem_orange.png`. We can make it so that each gem to collect is chosen
randomly. At the top of your code make the following change;

```python
# This is the old line
# from random import randrange

# Change it to this
from random import randrange, choice
```

This means that we will now use two functions, `randrange` and `choice` from the
`random` library.

Next, make a list of all the gem file names. This can go immediately after the
`WIDTH` and `HEIGHT` lines;

```python
GEMS = ['gem_blue', 'gem_yellow', 'gem_green', 'gem_orange']
```

Now add a new sprite for the gem;

```python
gem = Actor(choice(GEMS))
gem.x = randrange(0, WIDTH)
gem.y = randrange(0, HEIGHT)
```

This time instead of creating the `Actor` with a specific filename, as with the
player, the `choice` function is used to take one from the `GEMS` list.

Finally, remember to add `gem.draw()` to the `draw` function to make sure it
appears on the screen.

## Catch the gem

When the player gets the gem it should play a sound and then jump somewhere
else. This is all done in our `update` function, where you can add;

```python
def update():
    if keyboard[keys.RIGHT]:
        # etc
    # This is the new code
    if player.colliderect(gem):
        sounds.laser_large_1.play()
        gem.image = choice(GEMS)
        gems.pos = (randrange(0, WIDTH), randrange(0, HEIGHT))

```

## Add a score and a time limit

At the top of your code, after creating the `player` and `gem` sprites, make two**variables**;

```python
score = 0
timer = 30
```

These are going to keep track of the score the player has and how much time
there is remaining.

> ![NOTE]
> `score` and `timer` are named with lower case letters. This indicates that
> they are *variables*, meaning that they can change as the program runs.
> Compare this with `WIDTH`, `HEIGHT` and `GEMS`. These are called *constants*
> and once they have been set at the start they should never change.
> In fact, only the first character of the name matters to make something a
> variable or constant, so you could have a constant called `Width`, and you
> will often see variables like `scoreOne` and `scoreTwo`.

**Important:** To make sure that you can use these variables in different
functions list them as `global` in the `draw` and `update` functions, so that
they look like;

```python
def draw():
    global score, timer
    # etc

def update():
    global score, timer
    # etc
```

### Timer

The `update` function is called 60 times each second so to count down in
seconds each time 1/60 should be subtracted. Add this to your `update` function;

```python
    timer -= 1/60
```

and in the 'draw' function the time can be written at the top of the screen;

```python
    screen.draw.text("Time: " + str(timer), (10, 10), color="white")
```

The `screen.draw.text` allows you to put text anywhere on the screen and it must
have two arguments for the text to display, `"Time: " + str(timer)`, and the
position, `(10, 10)`. It can also optionally have some other arguments to
affect how the text appears, such as `color="white"`.

> ![NOTE]
> The optional arguments appear as `key=value` where `key` is what your are
> setting (`color` in this case - note the American spelling) and `value` is
> what you want to set it to (`"white"` in this case).
> Other keys you can try are `fontsize` and `background`.

You may see that the time appears with a long decimal part like `29.9333333`.
We get numbers like this because we are subtracting 1/60 from the timer each
time. It would be better if this appears like `29.9`. To do this, replace
`str(timer)` in the `screen.draw.text` line with `str(round(timer, 1)`

### Score

Now to keep track of the score. In the section of the `update` function where
the player catches the gem add `score += 1` to add 1 to the score. Then in the
`draw` function add a line to display the score, in a similar way that the
timer is displayed. This will not need to use `round` as it will always be a
round number.

> ![NOTE]
> A number like `29.933333`, with a decimal point, is called a *floating
> point number* or a *float*. These are used for data like distance and
> temperature, which are not normally exact whole numbers.
> A whole number, like `29` is called an *integer*. These are used for data
> that can be counted exactly, like a score or the number of people in a group.

## Ending the game

What happens when the time runs out? At the moment you will see that the time
keeps counting down into negative numbers! To fix this both the `draw` and
`update` functions need to have two parts, for when the game is being played
and when the game is over. They should look like this:

```python
def draw():
    global score, timer

    screen.clear()

    if timer > 0:
        # Game is being played
    else:
        # Game has finished

def update():
    global score, timer

    if timer > 0:
        # Game is being played
    else:
        # Game has finished
```

To start, Add the `if timer > 0:` to both your `draw` and `update` functions and
indent the rest of the contents of these functions, so they are inside this
`if`. Make sure that the `global` line and the `screen.clear()` line in `draw`
are not included in this.

> ![NOTE]
> In Thonny if you select several lines and press the 'Tab' key then all the
> lines will indent.

Test the game now and check that everything stops when the time runs out.

Instead of a blank screen it would be better to end with a message to give the
player's score. Add this to the `draw` function as an `else` section:

```python
def draw():
    global score, timer

    screen.clear()

    if timer > 0:
        # All the code for displaying the game in play
    else:
        # Display end of game message
```

## References

Gem images from the [Platformer Characters Pack](https://kenney.nl/assets/simplified-platformers-pack)
and player images from the [Scribble Dungeons](https://kenney.nl/assets/scribble-dungeons)
on [Kenney](https://kenney.nl). The licences for the images can be found
[here](images/Scribble-Dungeons-License.txt) and [here.](images/Simplified-Platformer-License.txt)

Sound files from [Sci-fi Sounds](https://kenney.nl/assets/sci-fi-sounds)
on [Kenney](https://kenney.nl). The licences for the images can be found
[here.](sounds/License.txt)
