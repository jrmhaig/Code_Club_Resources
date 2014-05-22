    def move(self):
        if self.move_left:
            if self.x > self.min_x:
                self.x = self.x - self.speed
            elif self.bounce:
                self.y = self.y + 5
                self.move_left = False
                self.move_right = True
        if self.move_right:
            if self.x < self.max_x:
                self.x = self.x + self.speed
            elif self.bounce:
                self.y = self.y + 5
                self.move_left = True
                self.move_right = False
        if self.move_up:                          # New
            if self.y > self.min_y:               # New
                self.y = self.y - self.speed      # New
