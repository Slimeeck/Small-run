from pygame import *

#Прописування можливостей для стін
class Wall(sprite.Sprite):
    def __init__ (self, rgb, x, y, w, h):
        super ().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w,h))
        self.wall.fill(rgb)

        self.block = Surface((self.width,self.height))
        self.block.fill(rgb)
        self.rect = self.block.get_rect()

        self.rect.x = x
        self.rect.y = y        
    def draw(self, window):
        window.blit(self.wall, (self.rect.x, self.rect.y))
