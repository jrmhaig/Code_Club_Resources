# Scrolling background

In some games, such as Mario, the player's character stays in the middle of the screen and the game moves around it. In this project we will see how that is done.

## Left-Right scroller starter project

To start, open this starter project and remix:

> https://scratch.mit.edu/projects/863782680/editor

Notice that this project has one sprite containing the background.

## Get the background scrolling to the left

The first thing to do is make the background scroll to the the left with this script:

![
When flag clicked
Go to x: [240] y: [0]
Forever
  Change x by [-5]
](./scroll1.svg)

This will get the background scrolling to the left but then it stops when it gets to the edge. To fix this, check its position after x has been changed by adding this inside the 'forever' loop and after the 'change x' block:


![
If (x position) < [-460] then
  Change x by [925]
](./scroll2.svg)

## Joining it up

At the moment the backgorund is not complete. We need to have two copies of it and we can do that by using **clones**.

*Change* your script in three ways;

* Use ![When I start as a clone](./when_i_start_as_a_clone.svg) instead of ![When flag clicked](./when_flag_clicked.svg)
* Remove ![Go to x: [240] y: [0]](./go_to_240_0.svg)
* Add ![Show](./show.svg) at the start

It should now look like this;

![
When I start as a clone
Show
Forever
  Change x by [-5]
  If (x position) < [-460] then
    Change x by [925]
](./scroll3.svg)

Then create a new script to create the two clones in the correct places;

![
When flag clicked
  Hide
  Go to x [240] y [0]
  Create clone of (myself)
  Go to x [-240] y [0]
  Create clone of (myself)
](.scroll4.svg)

## Get a sprite runing along the road

Choose a new sprite to run along the road. It is best to choose a sprite with walking costumes, such as;

* Avery Walking
* Bear-walking
* Cat
* Dog2
* Griffin
* Hare
* Hippo1
* Jaime
* Lion
* Mouse1
* Parrot
* Penguin
* Pico walking
* Polar Bear
* Shark
* Shark2
* Unicorn Running

Add a script to this sprite to make to run through all the cosumes so that it looks as though it is running. Note that we do not need to actually move the sprite.

![
When flag clicked
Go to x: [0] y: [-20]
Forever
  Next costume
](./scroll5.svg)

You might want to slow it down by adding a ![Wait [0.5] seconds](./wait_05_seconds.svg) in the right place.

## Challenges

1. Can you control the scrolling by pressing a button? (For example, the right arrow)
2. After the first challenge, can you get the scrolling to go the other way if you press a different button? (For example, the left arrow)
