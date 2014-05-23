...

class GamePiece:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.speed = 1
        self.image = image
        self.move_left = False
        self.move_right = False
        self.min_x = 10
        self.max_x = 340
        self.bounce = False                             # New

    def move(self):
        if self.move_left:
            if self.x > self.min_x:
                self.x = self.x - self.speed
            elif self.bounce:                           # New
                self.y = self.y + 5                     # New
                self.move_left = False                  # New
                self.move_right = True                  # New
        if self.move_right:
            if self.x < self.max_x:
                self.x = self.x + self.speed
            elif self.bounce:                           # New
                self.y = self.y + 5                     # New
                self.move_left = True                   # New
                self.move_right = False                 # New

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

...
