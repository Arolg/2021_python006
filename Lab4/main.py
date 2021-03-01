import pygame as pg
from pygame.draw import *

pg.init()
screen = pg.display.set_mode((400, 400))
screen.fill("#FFFFFF")
circle(screen, ("#FFF200"), (200, 200), 100)
line(screen, ("#000000"), (150, 250), (250, 250), 15)
circle(screen, ("#000000"), (150, 170), 10)
circle(screen, ("#FF0000"), (150, 170), 20)
circle(screen, ("#000000"), (150, 170), 10)
line(screen, ("#000000"), (100, 110), (180, 165), 7)
circle(screen, ("#FF0000"), (250, 170), 15)
circle(screen, ("#000000"), (250, 170), 7)
line(screen, ("#000000"), (300, 122), (220, 167), 7)
pg.display.update()

input()
