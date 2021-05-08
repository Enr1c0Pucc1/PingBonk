from pygame import *
w = 700
h = 500

class Alpha(sprite.Sprite):
    def __init__(self,x,y,h,w,speed,img_name):
        super().__init__()
        self.image = image.load(img_name)
        self.rect = Rect(x,y,h,w)
        self.rect.x
        self.rect.y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

ball=Alpha(100,100,5,5 ,1,"Tennis_Ball.png")

win = display.set_mode((w,h))
while True:
    win.fill((255,255,255))

    for e in event.get():
        if e.type == 12:
            exit()
    ball.reset()
    display.update()
