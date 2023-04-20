import pygame as pg
from InputBox import InputBox
from Button import Button

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

FONT = pg.font.Font('freesansbold.ttf', 20)
submit = Button(400,400,110,40)
input_box1 = InputBox(400, 100, 140, 32,'dodgerblue2','lightskyblue3')  # สร้าง InputBox1
input_box2 = InputBox(400, 200, 140, 32,'dodgerblue2','lightskyblue3')  # สร้าง InputBox2
input_box3 = InputBox(400, 300, 140, 32,'dodgerblue2','lightskyblue3')
input_boxes = [input_box1, input_box2, input_box3]  # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

def text(input_text,x,y,size,color):
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(input_text, True, color,(255,255,255))  # (text,is smooth?,letter color,background color)
    text_box = text.get_rect()  # สร้างสี่เหลี่ยมคลุม Text
    text_box.midleft = (x,y)
    screen.blit(text, text_box)


while run:
    screen.fill((255, 255, 255))
    text('Name : ', 400, 90, 20,(0, 0, 0))
    text('Surname : ', 400, 190, 20,(0, 0, 0))
    text('Age : ',400, 290,20,(0, 0, 0))

    submit.draw(screen,(0,0,0))
    submit_text = FONT.render('Submit', True,(255,255,255))
    submit_box = submit_text.get_rect()  # สร้างสี่เหลี่ยมคลุม Text
    submit_box.midleft = (420,420)
    screen.blit(submit_text, submit_box)


    for box in input_boxes:  # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update()  # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen)  # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    for event in pg.event.get():
        for (j, box) in enumerate(input_boxes):
            if event.type == pg.KEYDOWN:
                if j == 2:
                    if not event.unicode.isnumeric(): continue

            box.handle_event(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print("Hello " + input_box1.text + " " + input_box2.text + "! You are " + input_box3.text + " years old.")
                    input_box1.text = ''
                    input_box2.text = ''
                    input_box3.text = ''
                    event.key = None
                input_box1.txt_surface = input_box1.FONT.render(input_box1.text, True, input_box1.color)
                input_box2.txt_surface = input_box2.FONT.render(input_box2.text, True, input_box2.color)
                input_box3.txt_surface = input_box3.FONT.render(input_box3.text, True, input_box3.color)
            elif submit.isMouseOn():
                submit.draw(screen, (13, 85, 168))
                screen.blit(submit_text, submit_box)
                if event.type == pg.MOUSEBUTTONDOWN:
                    print(
                        "Hello " + input_box1.text + " " + input_box2.text + "! You are " + input_box3.text + " years old.")
                    input_box1.text = ''
                    input_box2.text = ''
                    input_box3.text = ''
                    break
                input_box1.txt_surface = input_box1.FONT.render(input_box1.text, True, input_box1.color)
                input_box2.txt_surface = input_box2.FONT.render(input_box2.text, True, input_box2.color)
                input_box3.txt_surface = input_box3.FONT.render(input_box3.text, True, input_box3.color)

        if event.type == pg.QUIT:
            pg.quit()
            run = False
        else:
            pg.display.update()