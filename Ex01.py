import pygame as pg
from Button import Button

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20, 20, 100, 100)  # สร้าง Object จากคลาส Button ขึ้นมา
while (run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.draw(screen,(164,159,165))
        if any(pg.mouse.get_pressed()):
            btn.draw(screen,(107,72,119))
    else:
        btn.draw(screen, (238, 58, 58))


    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False