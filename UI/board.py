import pygame, sys
import numpy as np

from UI.environment import initializeBoard

pygame.init()
screenHeight = 600
screenWidth = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Wumpus World')
screen.fill((240, 175, 10))


def makeTiles():

    lineClr = (54, 40, 5)

    pygame.draw.line(screen,lineClr,(50,50),(550,50),5)
    pygame.draw.line(screen, lineClr, (50, 550), (550, 550), 5)
    pygame.draw.line(screen, lineClr, (50, 50), (50, 550), 5)
    pygame.draw.line(screen, lineClr, (550, 50), (550, 550), 5)

    pygame.draw.line(screen, lineClr, (50, 100), (550, 100), 2)
    pygame.draw.line(screen, lineClr, (50, 150), (550, 150), 2)
    pygame.draw.line(screen, lineClr, (50, 200), (550, 200), 2)
    pygame.draw.line(screen, lineClr, (50, 250), (550, 250), 2)
    pygame.draw.line(screen, lineClr, (50, 300), (550, 300), 2)
    pygame.draw.line(screen, lineClr, (50, 350), (550, 350), 2)
    pygame.draw.line(screen, lineClr, (50, 400), (550, 400), 2)
    pygame.draw.line(screen, lineClr, (50, 450), (550, 450), 2)
    pygame.draw.line(screen, lineClr, (50, 500), (550, 500), 2)

    pygame.draw.line(screen, lineClr, (100, 50), (100, 550), 2)
    pygame.draw.line(screen, lineClr, (150, 50), (150, 550), 2)
    pygame.draw.line(screen, lineClr, (200, 50), (200, 550), 2)
    pygame.draw.line(screen, lineClr, (250, 50), (250, 550), 2)
    pygame.draw.line(screen, lineClr, (300, 50), (300, 550), 2)
    pygame.draw.line(screen, lineClr, (350, 50), (350, 550), 2)
    pygame.draw.line(screen, lineClr, (400, 50), (400, 550), 2)
    pygame.draw.line(screen, lineClr, (450, 50), (450, 550), 2)
    pygame.draw.line(screen, lineClr, (500, 50), (500, 550), 2)

    
def init():
    makeTiles()
    initializeBoard()
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                coordX = event.pos[0]
                coordY = event.pos[1]

                row = (coordY // 50)-1;
                col = (coordX // 50) - 1;

                print(row, col)