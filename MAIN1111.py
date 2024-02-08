from pygame import*
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        #
        sprite.Sprite.__init__(self)
        #
        self.image = transform.scale(
             image.load(player_image), (player_x, player_y))
        self.speed = player_speed
        #
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
             self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5:
             self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_width - 80:
             self.rect.y += self.speed
class Enemy(GameSprite):
    direction = "left"


    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.heigh = wall_height

        self.image = Surface((self.width, self.heigh))
        self.image.fill((color_1,color_2,color_3))

        self.rect = self.image.get_rect()
        self.rect.x =wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 900
win_heigth = 700
window = display.set_mode((win_width, win_heigth))
display.set_caption("Super game")
background = transform.scale(image.load("back.png"), (win_width, win_heigth))


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font. render('YOU LosE', True, (180, 0, 0 ))


'''mixer.init()
mixer.music.load("fonmusic.ogg")
mixer.music.play()'''
#boy1 = transform.scale(image.load(img_back), (win_width, win_height))
boy = Player('boy10.jpg' , 50, 75, 4)
boy.rect.x = 0
boy.rect.y = 0

Fredy = Enemy('Fredbear10.png', 50, 75, 4)
Fredy.rect.x = 100
Fredy.rect.y = 600

Bony = Enemy('Bony10.png', 50, 75, 4)
Bony.rect.x = 150
Bony.rect.y = 0

door=GameSprite("door1.png", 90, 100, 4)
door.rect.x = 800
door.rect.y = 600
final=False
#         цветцветцвет х    у    длинна  ширина 
Walls = []
w = Wall(0, 250, 154, 150, 87, 450, 7)
Walls.append(w)
w = Wall(0, 250, 154, 100, 195, 7, 400)
Walls.append(w)
w = Wall(0, 250, 154, 100, 595, 100, 7) 
Walls.append(w)
w = Wall(0, 250, 154, 200, 195, 7, 410)
Walls.append(w)
w = Wall(0, 250, 154, 200, 195, 100, 7)
Walls.append(w)
w = Wall(0, 250, 154, 300, 195, 7, 400)
Walls.append(w)
w = Wall(0, 250, 154, 400, 87, 7, 450)
Walls.append(w)
w = Wall(0, 250, 154, 750, 590, 380, 7)
Walls.append(w)
w = Wall(0, 250, 154, 600, 500, 7, 380)
Walls.append(w)
w = Wall(0, 250, 154, 540, 390, 380, 7)
Walls.append(w)
w = Wall(0, 250, 154, 300, 390, 100, 7)
Walls.append(w)
w = Wall(0, 250, 154, 100, 195, 7, 400)
Walls.append(w)
w = Wall(0, 250, 154, 500, 300, 400, 7)
Walls.append(w)
w = Wall(0, 250, 154, 720, 10, 7, 200)
Walls.append(w)
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish !=True:
    
        window.blit(background,(0, 0))
        boy.update()
        Bony.update()
        Fredy.update()
        door.update()

##
        boy.reset()
        Bony.reset()
        Fredy.reset()
        door.reset()
    
    for e in Walls:
        e.draw_wall()
        if sprite.collide_rect(boy,e):
            #boy = Player('boy10.jpg' , 50, 75, 4)
            boy.rect.x = 0
            boy.rect.y = 0
        


    if sprite.collide_rect(boy,Bony ) or sprite.collide_rect(boy, Fredy ):
        finish = True
        window.blit(lose, (400, 200))

    if sprite.collide_rect(boy, door):
        finish = True
        window.blit(win, (200,200))
    
    display.update()
    clock.tick(FPS)