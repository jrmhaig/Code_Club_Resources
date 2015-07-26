    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = 0
        self.bounce = False
        self.image = image
        self.min_y = 20                   # New
        self.min_x = 10
        self.max_x = 340
