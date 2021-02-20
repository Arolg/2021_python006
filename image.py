import pygame

screen = pygame.display.set_mode((600, 400))
image = pygame.image.load("2_2.png")
screen.blit(image, (100, 50))
pygame.display.update()