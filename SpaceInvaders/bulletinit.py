    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.speed = 1
        self.image = image
        self.move_left = False
        self.move_right = False
        self.move_up = False              # New
        self.min_y = 20                   # New
        self.min_x = 10
        self.max_x = 340
        self.bounce = False
