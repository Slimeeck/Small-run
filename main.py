from pygame import *
from player import Player
from sprite import GameSprite 
from wall import *

win_width = 700
win_height = 700
#Створення усього на екрані (та сам екран)
font.init()
window = display.set_mode((win_width, win_height))
display.set_caption("Run")
background = transform.scale(image.load("Maze_bg.png"), (win_width, win_height))
strawberry1 = GameSprite("Strawberry.png", 32, 32, 250, 400)
strawberry2 = GameSprite("Strawberry.png", 32, 32, 200, 300)
strawberry3 = GameSprite("Strawberry.png", 32, 32, 150, 400)
strawberry4 = GameSprite("Strawberry.png", 32, 32, 350, 200)
player = Player("Pong_ball.png", 20, 20, 60, 60)

points = 0

#Процеси
game = True
clock = time.Clock()
FPS = 60





#Стіни
#1
block1 = Wall((102, 102, 0), 0,0,800,20)
block2 = Wall((102, 102, 0), 0,0,10,800)
block5 = Wall((102, 102, 0), 690,5,20,700)
block6 = Wall((102, 102, 0), 0,590,700,30)
#2
block3 = Wall((102, 102, 0), 200,100,50,100)
block4 = Wall((102, 102, 0), 200,100,400,10)
block7 = Wall((102, 102, 0), 400,300,30,200)
block8 = Wall((102, 102, 0), 300,450,20,200)
block9 = Wall((102, 102, 0), 0,0,10,10)
block10 = Wall((102, 102, 0), 0,0,10,10)
block11 = Wall((102, 102, 0), 100,100,40,360)
block12 = Wall((102, 102, 0), 100,260,500,25)

time.set_timer(USEREVENT, 1000)
font1 = font.SysFont('Arial', 30)
counter = 0



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == USEREVENT:
            counter += 1


    window.blit(background,(0, 0))
    window.blit(font1.render(str(counter), True, (155, 50, 222)), (32, 48))
    player.draw(window)
    player.move()
#Колайдери
    if sprite.collide_rect(player, block1) or sprite.collide_rect(player, block2) or sprite.collide_rect(player, block3) or sprite.collide_rect(player, block4) or sprite.collide_rect(player, block5) or sprite.collide_rect(player, block6) or sprite.collide_rect(player, block7) or sprite.collide_rect(player, block8) or sprite.collide_rect(player, block9) or sprite.collide_rect(player, block10) or sprite.collide_rect(player, block11) or sprite.collide_rect(player, block12):
        player.rect.x = 20
        player.rect.y = 60

    if sprite.collide_rect(player, strawberry1):
        strawberry1.rect.x = 30
        strawberry1.rect.y = 0

    if sprite.collide_rect(player, strawberry2):
        strawberry2.rect.x = 40
        strawberry2.rect.y = 0

    if sprite.collide_rect(player, strawberry3):
        strawberry3.rect.x = 50
        strawberry3.rect.y = 0

    if sprite.collide_rect(player, strawberry4):
        strawberry4.rect.x = 60
        strawberry4.rect.y = 0


        points = +1

#Промальовувуння усього
    block1.draw(window)
    block2.draw(window)
    block3.draw(window)
    block4.draw(window)
    block5.draw(window) 
    block6.draw(window)
    block7.draw(window)
    block8.draw(window)
    block9.draw(window)
    block10.draw(window)
    block11.draw(window)
    block12.draw(window)
    strawberry1.draw(window)
    strawberry2.draw(window)
    strawberry3.draw(window)
    strawberry4.draw(window)

    display.update()
    clock.tick(FPS)
