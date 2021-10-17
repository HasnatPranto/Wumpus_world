import pygame, sys
import numpy as np

from Logic.logic import *
from UI.environment import initializeBoard, doReset, recreateEnv, updateHunter, wumpus_isDead, changeDir, board

pygame.init()
screenHeight = 650
screenWidth = 1100
LgCOLR = (255, 255, 255)
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Wumpus World')
wum_pic = pygame.image.load("./UI/assets/wumpus.jpg")
hunter_pic = pygame.image.load("./UI/assets/hunter.jpg")
treasure_pic = pygame.image.load("./UI/assets/treasure.jpg")
pit_pic = pygame.image.load("./UI/assets/pit.png")
screen.fill((5, 48, 0))
pygame.draw.rect(screen, (1, 5, 0), [50, 10, 600, 600])
X_COORD = 52
Y_COORD = 552
Hunter_POS = 90
arrow = 1
deg = 0

begin_button = pygame.draw.rect(screen, (157, 252, 3), (790, 550, 70, 35));
reset_button = pygame.draw.rect(screen, (252, 215, 3), (885, 550, 70, 35));
font = pygame.font.SysFont('freesans', 18)
lbl_begin = font.render('Begin', True, (5, 48, 0))
lbl_reset = font.render('Reset', True, (5, 48, 0))
screen.blit(lbl_begin, (806, 557))
screen.blit(lbl_reset, (901, 557))


def makeTiles():
    boxClr = (54, 40, 5)
    lineClr = (252, 59, 0)

    pygame.draw.line(screen, boxClr, (50, 10), (650, 10), 5)
    pygame.draw.line(screen, boxClr, (50, 610), (650, 610), 5)
    pygame.draw.line(screen, boxClr, (50, 10), (50, 610), 5)
    pygame.draw.line(screen, boxClr, (650, 10), (650, 610), 5)

    pygame.draw.line(screen, lineClr, (50, 70), (650, 70), 2)
    pygame.draw.line(screen, lineClr, (50, 130), (650, 130), 2)
    pygame.draw.line(screen, lineClr, (50, 190), (650, 190), 2)
    pygame.draw.line(screen, lineClr, (50, 250), (650, 250), 2)
    pygame.draw.line(screen, lineClr, (50, 310), (650, 310), 2)
    pygame.draw.line(screen, lineClr, (50, 370), (650, 370), 2)
    pygame.draw.line(screen, lineClr, (50, 430), (650, 430), 2)
    pygame.draw.line(screen, lineClr, (50, 490), (650, 490), 2)
    pygame.draw.line(screen, lineClr, (50, 550), (650, 550), 2)

    pygame.draw.line(screen, lineClr, (110, 10), (110, 610), 2)
    pygame.draw.line(screen, lineClr, (170, 10), (170, 610), 2)
    pygame.draw.line(screen, lineClr, (230, 10), (230, 610), 2)
    pygame.draw.line(screen, lineClr, (290, 10), (290, 610), 2)
    pygame.draw.line(screen, lineClr, (350, 10), (350, 610), 2)
    pygame.draw.line(screen, lineClr, (410, 10), (410, 610), 2)
    pygame.draw.line(screen, lineClr, (470, 10), (470, 610), 2)
    pygame.draw.line(screen, lineClr, (530, 10), (530, 610), 2)
    pygame.draw.line(screen, lineClr, (590, 10), (590, 610), 2)

    pygame.display.update()


def setLegends():
    global wum_pic, hunter_pic, treasure_pic, pit_pic

    wum_pic = pygame.transform.scale(wum_pic, (40, 40))
    hunter_pic = pygame.transform.scale(hunter_pic, (40, 40))
    treasure_pic = pygame.transform.scale(treasure_pic, (40, 40))
    pit_pic = pygame.transform.scale(pit_pic, (40, 40))
    screen.blit(wum_pic, (700, 10))
    screen.blit(hunter_pic, (700, 55))
    screen.blit(treasure_pic, (700, 100))
    screen.blit(pit_pic, (700, 145))
    pygame.draw.circle(screen, (232, 15, 0), (720, 210), 10)
    pygame.draw.circle(screen, (252, 193, 1), (720, 240), 10)
    pygame.draw.circle(screen, (29, 182, 224), (720, 270), 10)
    pygame.draw.circle(screen, (66, 230, 7), (720, 300), 10)

    font = pygame.font.SysFont('freesans', 15)

    legend_wumpus = font.render('Wumpus', True, LgCOLR)
    legend_hunter = font.render('Hunter', True, LgCOLR)
    legend_pit = font.render('Pit', True, LgCOLR)
    legend_treasure = font.render('Treasure', True, LgCOLR)
    legend_stench = font.render('Stench', True, LgCOLR)
    legend_breeze = font.render('Breeze', True, LgCOLR)
    legend_glitter = font.render('Glitter', True, LgCOLR)
    legend_safe = font.render('Safe', True, LgCOLR)

    screen.blit(legend_wumpus, (775, 20))
    screen.blit(legend_hunter, (775, 65))
    screen.blit(legend_treasure, (775, 110))
    screen.blit(legend_pit, (775, 155))
    screen.blit(legend_stench, (775, 200))
    screen.blit(legend_glitter, (775, 231))
    screen.blit(legend_breeze, (775, 261))
    screen.blit(legend_safe, (775, 291))

    pygame.draw.rect(screen, (0, 2, 18), [935, 15, 115, 40])
    font = pygame.font.SysFont('freesans', 20)
    lbl_arrow = font.render('Arrow: ', True, (254, 0, 5))
    lbl_acont = font.render(str(arrow), True, (254, 0, 5))
    screen.blit(lbl_arrow, (960, 22))
    screen.blit(lbl_acont, (1010, 22))


def originFill():
    screen.fill((5, 48, 0))
    pygame.draw.rect(screen, (1, 5, 0), [50, 10, 600, 600])
    begin_button = pygame.draw.rect(screen, (157, 252, 3), (790, 550, 70, 35));
    reset_button = pygame.draw.rect(screen, (252, 215, 3), (885, 550, 70, 35));
    font = pygame.font.SysFont('freesans', 18)
    lbl_begin = font.render('Begin', True, (5, 48, 0))
    lbl_reset = font.render('Reset', True, (5, 48, 0))
    screen.blit(lbl_begin, (806, 557))
    screen.blit(lbl_reset, (901, 557))

    makeTiles()
    setLegends()


def gameOverDialogue(result):
    pygame.draw.rect(screen, (1, 5, 0), [100, 300, 300, 100])

def takeNextMove(newDirection,newPosition, move):

    global deg,Hunter_POS
    rotation = abs(newDirection-deg)

    if (newDirection > deg):
        for i in range(0, rotation):
            deg = changeDir(screen, "left", Hunter_POS)
    elif (newDirection < deg):
        for i in range(0, rotation):
            deg = changeDir(screen, "right", Hunter_POS)

    if move==True:
        b = updateHunter(Hunter_POS, newPosition, screen)
        originFill()
        recreateEnv(screen)
        Hunter_POS = newPosition
        update_knowledge_base_with_current_position_info(board[Hunter_POS])


def init():
    global X_COORD, Y_COORD, Hunter_POS, arrow, direction, deg
    originFill()
    initializeBoard(screen)

    update_knowledge_base_with_current_position_info(board[90])

    while True:
        pygame.display.update()

        for event in pygame.event.get():

            pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    # direction == "right":
                    if deg == 0:
                        if Hunter_POS + 1 < 100:
                            Hunter_POS += 1
                            originFill()
                            recreateEnv(screen)
                            b = updateHunter(Hunter_POS - 1, Hunter_POS, screen)

                            # update_knowledge_base_with_current_position_info(str(Hunter_POS), board[Hunter_POS])

                    # direction == "left":
                    if deg == 180:
                        if Hunter_POS - 1 >= 0:
                            Hunter_POS -= 1
                            originFill()
                            recreateEnv(screen)
                            b = updateHunter(Hunter_POS + 1, Hunter_POS, screen)

                            # update_knowledge_base_with_current_position_info(str(Hunter_POS), board[Hunter_POS])

                    # direction == "up":
                    if deg == 90:
                        if Hunter_POS - 10 >= 0:
                            Hunter_POS -= 10
                            originFill()
                            recreateEnv(screen)
                            b = updateHunter(Hunter_POS + 10, Hunter_POS, screen)
                            if b != None:
                                gameOverDialogue(b)

                            # update_knowledge_base_with_current_position_info(str(Hunter_POS), board[Hunter_POS])

                    # direction == "down":
                    if deg == 270:
                        if Hunter_POS + 10 < 100:
                            Hunter_POS += 10
                            originFill()
                            recreateEnv(screen)
                            b = updateHunter(Hunter_POS - 10, Hunter_POS, screen)

                    update_knowledge_base_with_current_position_info(board[Hunter_POS])

                if event.key == pygame.K_LEFT:
                    deg = changeDir(screen, "left", Hunter_POS)

                if event.key == pygame.K_RIGHT:
                    deg = changeDir(screen, "right", Hunter_POS)
                    # print(deg)

            if event.type == pygame.MOUSEBUTTONDOWN:

                click = event.pos

                if reset_button.collidepoint(click):
                    X_COORD = 52
                    Y_COORD = 552
                    Hunter_POS = 90
                    arrow = 1
                    doReset()
                    originFill()
                    initializeBoard(screen)

                if begin_button.collidepoint(click):
                    wumpus_isDead(screen)
                    arrow -= 1
                    originFill()
                    recreateEnv(screen)
                    updateHunter(Hunter_POS, Hunter_POS, screen)

            '''if event.type ==pygame.MOUSEBUTTONDOWN:
                coordX = event.pos[0]
                coordY = event.pos[1]
                coordY-=10
                coordX-=50
                row = (coordY // 60);
                col = (coordX // 60);

                print(row, col)
                #pygame.draw.circle(screen, (0, 255, 0), (600, 500), 15)'''
