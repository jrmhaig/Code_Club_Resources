    def move(self, direction = None):
        if direction == None:
            # The function was called as: move()
            direction = self.direction

        if direction == LEFT:
            if self.x > self.min_x:
                self.x = self.x - self.speed
            elif self.bounce:
                self.y = self.y + 5
                self.direction = RIGHT
        elif direction == RIGHT:
            if self.x < self.max_x:
                self.x = self.x + self.speed
            elif self.bounce:
                self.y = self.y + 5
                self.direction = LEFT
        elif direction == UP:                         # New
            if self.y > self.min_y:                   # New
                self.y = self.y - self.speed          # New
