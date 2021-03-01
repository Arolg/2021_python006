import pygame
from pygame.draw import *

GREEN = "#008000"
BROWN = "#b15124"
RED = "#FF0000"
TEAL = "#008080"
SKY = "#87CEEB"
BLACK = "#000000"
FPS = 30
pygame.init()
screen = pygame.display.set_mode((800, 600))
polygon(screen, SKY, [[0, 0], [0, 300], [800, 300], [800, 0]])
polygon(screen, GREEN, [[0, 600], [0, 300], [800, 300], [800, 600]])

polygon(screen, RED, [[250, 320], [100, 320], [175, 250]])
polygon(screen, BROWN, [[250, 320], [250, 420], [100, 420], [100, 320]])
polygon(screen, TEAL, [[195, 350], [195, 380], [155, 380], [155, 350]])

polygon(screen, RED, [[600, 310], [470, 310], [535, 240]])
polygon(screen, BROWN, [[600, 310], [600, 390], [470, 390], [470, 310]])
polygon(screen, TEAL, [[550, 340], [550, 360], [520, 360], [520, 340]])

line(screen, BLACK, (310, 410), (310, 330), 10)
circle(screen, GREEN, (150, 170), 20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
