import pygame as pg
from pygame.draw import *

size = [630,500]

pg.init()
finished = False

s = pg .display.set_mode(size)
clock = pg.time.Clock()
BLUE = (0,  0, 255)

s.fill(BLUE)
rect(s, (0, 225, 0), (0, 200, 630, 630))
rect(s, (100,105, 0), (50,160 , 200, 170))
rect(s, (90, 100, 255), (86, 176, 122, 115))
polygon(s,(255,0,0),[[51,160],[250,160],[145,60]],3)
line(s,(0,0,0),(461,145),(461,310),19)
circle(s,(0,100,0),(461,125),40)
circle(s,(0,100,0),(461,75),40)
circle(s,(0,100,0),(421,100),40)
circle(s,(0,100,0),(501,100),40)
circle(s,(0,100,0),(421,145),40)
circle(s,(0,100,0),(501,145),40)
circle(s,(244,244,244),(321,80),30)
circle(s,(244,244,244),(291,80),30)
circle(s,(244,244,244),(261,80),30)
circle(s,(244,244,244),(231,80),30)
circle(s,(244,244,244),(250,50),30)
circle(s,(244,244,244),(295,50),30)
circle(s,(255,195,0),(600,55),30)
pg.display.update()

while not finished:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True



















