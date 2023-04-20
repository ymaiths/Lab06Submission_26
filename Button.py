import pygame as pg
from Rectangle import Rectangle as Rec

class Button(Rec):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rec.__init__(self, x, y, w, h)

    def isMouseOn(self):
        (pos_x,pos_y) = pg.mouse.get_pos()
        if (pos_x >= self.x) and (pos_x <= self.x+self.w) and (pos_y >= self.y) and (pos_y <= self.y+self.w):
            return True