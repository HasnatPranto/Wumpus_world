import pygame, sys
import numpy as np

from Logic.logic import *
from UI.environment import initializeBoard, doReset, recreateEnv, updateHunter, wumpus_isDead, changeDir, board, \
    checkGameOver

# initializing pygame
pygame.init()

# screen constraints
screen_height = 650
screen_width = 1100

# variables
LgCOLR = (255, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
yellow = (210, 210, 0)
light_yellow = (255, 255, 0)

# initializing font object
small_font = pygame.font.SysFont('arial', 25)
medium_font = pygame.font.SysFont('arial', 40)
large_font = pygame.font.SysFont('arial', 80)

# screen details
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Wumpus World')

# images
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

# buttons
begin_button = pygame.draw.rect(screen, (157, 252, 3), (790, 550, 70, 35))
reset_button = pygame.draw.rect(screen, (252, 215, 3), (885, 550, 70, 35))
new_game_button = pygame.draw.rect(screen, light_yellow, (680, 550, 180, 40))
quit_game_button = pygame.draw.rect(screen, light_yellow, (880, 550, 180, 40))

# fonts
font = pygame.font.SysFont('freesans', 18)
lbl_begin = font.render('Begin', True, (5, 48, 0))
lbl_reset = font.render('Reset', True, (5, 48, 0))
screen.blit(lbl_begin, (806, 557))
screen.blit(lbl_reset, (901, 557))

# game state variables
game_over_state = False
new_game_state = False
quit_game_state = False
game_win_state = None


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
    begin_button = pygame.draw.rect(screen, (157, 252, 3), (790, 550, 70, 35))
    reset_button = pygame.draw.rect(screen, (252, 215, 3), (885, 550, 70, 35))
    font = pygame.font.SysFont('freesans', 18)
    lbl_begin = font.render('Begin', True, (5, 48, 0))
    lbl_reset = font.render('Reset', True, (5, 48, 0))
    screen.blit(lbl_begin, (806, 557))
    screen.blit(lbl_reset, (901, 557))

    makeTiles()
    setLegends()


def gameOverDialogue(result):
    pygame.draw.rect(screen, (1, 5, 0), [100, 300, 300, 100])


def text_objects(text, color, size):
    if size == 'small':
        text_surface = small_font.render(text, True, color)
    elif size == 'medium':
        text_surface = medium_font.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


def text_to_button(msg, color, button_x, button_y, button_width, button_height, size="medium"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    screen.blit(text_surf, text_rect)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    global game_over_state, quit_game_state, new_game_state
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        # if click[0] == 1 and action is not None:
        #     if action == 'quit':
        #         quit_game_state = True
        #     elif action == 'reset':
        #         new_game_state = True
        #         # set reset logic here
        #         print('reset')
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def message_to_screen(msg, color, y_displace=0, size='medium'):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = screen_width * 0.8, screen_height * 0.7 + y_displace
    screen.blit(text_surf, text_rect)


def takeNextMove(new_direction, new_position, move):
    global deg, Hunter_POS
    rotation = abs(new_direction - deg) / 90

    if new_direction > deg:
        for i in range(0, rotation):
            deg = changeDir(screen, "left", Hunter_POS)
    elif new_direction < deg:
        for i in range(0, rotation):
            deg = changeDir(screen, "right", Hunter_POS)

    # if move == true
    if move:
        originFill()
        recreateEnv(screen)
        b = updateHunter(Hunter_POS, new_position, screen)
        Hunter_POS = new_position
        update_knowledge_base_with_current_position_info(board[Hunter_POS])


def init():
    global X_COORD, Y_COORD, Hunter_POS, arrow, deg, game_over_state, new_game_state, quit_game_state, game_win_state
    originFill()
    initializeBoard(screen)
    initKB()
    update_knowledge_base_with_current_position_info(board[90])

    # game loop
    while True:
        # if game is over, display a message
        if game_over_state:
            if not game_win_state:
                message_to_screen('You Lost!', red, y_displace=-20, size='large')
            if game_win_state:
                message_to_screen('You Won!', red, y_displace=-20, size='large')
            pygame.display.update()

        # game over loop
        while game_over_state:
            button('New Game', 680, 550, 180, 40, yellow, light_yellow, action='reset')
            button('Quit Game', 880, 550, 180, 40, yellow, light_yellow, action='quit')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = event.pos
                    print(click)
                    if 680 <= click[0] <= 860 and 550 <= click[1] <= 590:
                        print('new game')
                        # write logic for new game
                    if 880 <= click[0] <= 1060 and 550 <= click[1] <= 590:
                        print('quit game')
                        pygame.quit()
                        quit()
        pygame.display.update()

        # event loop
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

                            # update_knowledge_base_with_current_position_info(str(Hunter_POS), board[Hunter_POS])

                    # direction == "down":
                    if deg == 270:
                        if Hunter_POS + 10 < 100:
                            Hunter_POS += 10
                            originFill()
                            recreateEnv(screen)
                            b = updateHunter(Hunter_POS - 10, Hunter_POS, screen)
                    update_knowledge_base_with_current_position_info(board[Hunter_POS])

                    gg = checkGameOver(Hunter_POS)
                    if gg == 'dead':
                        lost = 1
                        # write your code here
                        game_over_state = True
                        game_win_state = False

                    if gg == 'victory':
                        victory = 1
                        # write your code here
                        game_over_state = True
                        game_win_state = True

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
                    deg = 0
                    doReset()
                    originFill()
                    initializeBoard(screen)
                    initKB()

                if begin_button.collidepoint(click):
                    wumpus_isDead(screen)
                    arrow -= 1
                    originFill()
                    recreateEnv(screen)
                    updateHunter(Hunter_POS, Hunter_POS, screen)
                    gameOver = True

            '''if event.type ==pygame.MOUSEBUTTONDOWN:
                coordX = event.pos[0]
                coordY = event.pos[1]
                coordY-=10
                coordX-=50
                row = (coordY // 60);
                col = (coordX // 60);

                print(row, col)
                #pygame.draw.circle(screen, (0, 255, 0), (600, 500), 15)'''
