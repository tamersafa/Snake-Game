import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)   ## Grid Lines
BLACK = (0,0,0)         ## Grid Cell
RED = (255,0,0)         ## Snake
GREEN = (0,255,0)       ## Food

FPS = 10

WIDTH, HEIGHT = 700,550

BLOCKSIZE = 15 

TOOLBAR_HEIGHT = HEIGHT - WIDTH

BORDER = pygame.rect.Rect(WIDTH, HEIGHT, BLOCKSIZE, BLOCKSIZE)

