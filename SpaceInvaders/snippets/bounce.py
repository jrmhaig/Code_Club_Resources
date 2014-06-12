...

class GamePiece:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = 0                              # New
        self.bounce = False                             # New
        self.image = image
        self.min_x = 10
        self.max_x = 340

    def move(self, direction = None):                   # Changed
        if direction == None:                           # New
            # The function was called as: move()        # New
            direction = self.direction                  # New

        if direction == LEFT:
            if self.x > self.min_x:
                self.x = self.x - self.speed
            elif self.bounce:                           # New
                self.y = self.y + 5                     # New
                self.direction = RIGHT                  # New
        elif direction == RIGHT:
            if self.x < self.max_x:
                self.x = self.x + self.speed
            elif self.bounce:                           # New
                self.y = self.y + 5                     # New
                self.direction = LEFT                   # New

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

...
