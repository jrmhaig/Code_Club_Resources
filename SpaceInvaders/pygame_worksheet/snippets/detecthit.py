class GamePiece:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = 0                              # New
        self.height = 0                             # New
...

    def draw(self):
        self.blit(self.image, (self.x, self.y))

    def detect_hit(self, other):                    # New
        if other.x > self.x \                       # New
                and other.x < self.x + self.width \ # New
                and other.y > self.y \              # New
                and other.y < self.y + self.height: # New
            return True                             # New
        else:                                       # New
            return False                            # New
...
# Make the alien move by itself
alien.direction = LEFT
# Make the alien bounce when it hits the edge
alien.bounce = True
alien.speed = 0.3
# Set the height and width of the alien             # New
alien.width = 47                                    # New
alien.height = 22                                   # New
