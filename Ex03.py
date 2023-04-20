import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('FRA 142', True, (255, 255, 255), (0, 0, 0)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() #สร้างสี่เหลี่ยมคลุม Text
textRect.center = (win_x // 2, win_y // 2)


while (run):
    screen.fill((176, 80, 210))
    screen.blit(text, textRect)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

