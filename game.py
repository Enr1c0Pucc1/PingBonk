from pygame import *
w = 700
h = 500

win = display.set_mode((w,h))
while True:
    win.fill((255,255,255))

    for e in event.get():
        if e.type == 12:
            exit()
    
    display.update()