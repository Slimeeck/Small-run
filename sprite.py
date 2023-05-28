from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img_name, width, height, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

        