from pygame import *
from sprite import GameSprite 
#Змінні для головного героя
class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 10:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y < 800 - 80:
            self.rect.y -= self.speed

            