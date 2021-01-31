import time

class Robot:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 512 / 2
        self.rect.y = 512 / 2
        self.rect.center = self.rect.x, self.rect.y

    def move(self):
        pass

