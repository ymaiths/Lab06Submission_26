import pygame as pg


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self,screen,colour=(120,20,220)):
        pg.draw.rect(screen,colour,(self.x,self.y,self.w,self.h))
