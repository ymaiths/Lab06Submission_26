import pygame as pg
from Button import Button

pg.init()
right,left,up,down = False,False,False,False
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20, 20, 100, 100)  # สร้าง Object จากคลาส Button ขึ้นมา
while (run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                right = True
                #btn.x += 1
            if event.key == pg.K_a:
                left = True
                #btn.x -= 1
            if event.key == pg.K_w:
                up = True
                #btn.y -= 1
            if event.key == pg.K_s:
                down = True
                #btn.y += 1
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                right = False
            if event.key == pg.K_a:
                left = False
            if event.key == pg.K_w:
                up = False
            if event.key == pg.K_s:
                down = False
        if right:
            btn.x += 1
        if left:
            btn.x -= 1
        if up:
            btn.y -= 1
        if down:
            btn.y += 1

    pg.display.update()

