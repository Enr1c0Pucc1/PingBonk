from pygame import *
from random import random
w=1280
h=720
q = 10
a = 10
score1 = 0
score2 = 0


class Main(sprite.Sprite):

    def __init__(self,x,y,filename,speed,v,n):
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(v,n))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.n = n
        self.v = v
        self.hface = "right"
        self.nface = "up"
        self.speed = speed

    def reset(self):
        win.blit(self.image,( self.rect.x,self.rect.y))

class Ball(Main):
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False
        self.last_touch_racket = False

    def change_speed(self):
        self.speed += 3
        self.need_change_speed = True

    def goto(self):
        global pscore1
        global pscore2
        global score1
        global score2
        global end_game
        if sprite.collide_rect(self,side_stena):
            self.rect.x = 1100
            self.rect.y = h*0.5
            score2 += 1
            pscore2 = scndshirift.render("Счет: "+str(score2),False,CornflowerBlue)
        if sprite.collide_rect(self,side_stena1):
            self.rect.x = 100
            self.rect.y = h*0.5
            score1 += 1
            pscore1 = scndshirift.render("Счет: "+str(score1),False,CornflowerBlue)         
        if score1 >= 15:
            end_game = lose_text2
        if score2 >= 15:
            end_game = lose_text1
    def update(self):
        if self.need_change_speed:
            self.speed -= 0.1
            if self.speed < q:
                self.speed = 10
                self.need_change_speed = False

        if self.hface == "right":
            self.rect.x += self.speed
            if sprite.collide_rect(self,racketka_right):
                self.last_touch_racket = "right"
                self.change_speed()
                self.hface="left"
                if random() > 0.5:
                    self.nface = "up"
        else:
            self.rect.x -= self.speed
            if sprite.collide_rect(self,racketka_left):
                self.last_touch_racket = "left"
                self.change_speed()
                self.hface="right" 
                if random() > 0.5:
                    self.nface = "down" 
        if self.nface == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.nface="down"
        else:
            self.rect.y += self.speed
            if self.rect.y + self.n > h:
                self.nface="up" 
        self.reset()

class Racketka(Main):
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False

    def change_speed(self):
        self.speed -= 5
        self.need_change_speed = True

    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + 160 > h:
            self.rect.y = h - 160
        if self.need_change_speed:
            self.speed += 0.01
            if self.speed > a:
                self.speed = a
                self.need_change_speed = False

        keys=key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        self.reset()

class Racketka1(Main):
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False

    def change_speed(self):
        self.speed -= 5
        self.need_change_speed = True

    
    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + 160 > h:
            self.rect.y = h - 160
        if self.need_change_speed:
            self.speed += 0.01
            if self.speed > a:
                self.speed = a
                self.need_change_speed = False

        keys=key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        self.reset()

class Wall(sprite.Sprite):  

    def __init__(self,x,y,w,h,side,color):  
        self.image = Surface((w,h))   
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        if sprite.collide_rect(self,ball):   
            self.reset()

ball = Ball(x= 200,y = 540,filename="Tennis_Ball.png",speed = q,v = 75,n = 75)
racketka_left = Racketka(x = 10,y=540,filename="Чимс1.png",speed = a,v = 100,n = 160)
racketka_right = Racketka1(x = w-100,y = 540,filename="Чимс2.png",speed = a,v = 100,n = 160)

CornflowerBlue = (100,149,237)   
Black = (255,255,255)  
PeachPuff = (255,218,185)

side_stena = Wall(0,0,1,1080,0,PeachPuff)     
side_stena1 = Wall(w-1,0,1,1080,1,PeachPuff)   

resolution = [w,h]

win = display.set_mode((resolution),flags=FULLSCREEN)
display.set_caption("PingBonk")

timer = time.Clock()
FPS = 60

fon=image.load("fon.png")

font.init()
shirift = font.SysFont("Impact",100)
lose_text1 = shirift.render("Игрок слева проиграл!",False,Black)

lose_text2 = shirift.render("Игрок справа проиграл!",False,Black)

scndshirift = font.SysFont("Impact",50)
pscore1 = scndshirift.render("Счет: "+str(score2),False,CornflowerBlue)

pscore2 = scndshirift.render("Счет: "+str(score1),False,CornflowerBlue)

game = True
end_game = False
while game:
    for e in event.get():
        if e.type == 2:
            keys=key.get_pressed()
            if keys[K_ESCAPE]:
                game = False
        if e.type == 12:
            game = False

    win.blit(fon,(0,0))
    timer.tick(FPS)   

    if end_game == False:
        ball.update() 
        ball.goto()
        racketka_left.update()
        racketka_right.update()
        side_stena.update()
        side_stena1.update()
        win.blit(pscore1,(0,0))
        win.blit(pscore2,(w-175,0))
    if end_game == lose_text1:
        win.blit(lose_text1,(w*0.2,h*0.2))
    if end_game == lose_text2:
        win.blit(lose_text2,(w*0.2,h*0.2))
    display.update()
