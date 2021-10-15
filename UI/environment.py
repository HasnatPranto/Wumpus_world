import numpy as np
import random
import pygame

hunter_pos,safe,treasure,pit,wumpus, breeze, glitter, stench, max_pit,board_size = "hunter","safe","treasure","pit","wumpus","breeze","glitter","stench",10,10
arrow = True
wum_pos =0

def setPic(wp,pp,tp,hp):

    wum_pic = wp
    pit_pic = pp
    treasure_pic = tp
    hunter_pic = hp

wum_pic = pygame.image.load("./UI/assets/wumpus.jpg")
wum_pic = pygame.transform.scale(wum_pic, (58, 58))
wumDead_pic = pygame.image.load("./UI/assets/dead_wumpus.png")
wumDead_pic = pygame.transform.scale(wumDead_pic, (58, 58))
pit_pic = pygame.image.load("./UI/assets/pit.png")
pit_pic = pygame.transform.scale(pit_pic, (58, 58))
treasure_pic = pygame.image.load("./UI/assets/treasure.jpg")
treasure_pic = pygame.transform.scale(treasure_pic, (58, 58))
hunter_pic = pygame.image.load("./UI/assets/hunter.jpg")
hunter_pic = pygame.transform.scale(hunter_pic, (58, 58))
hunter_pic_D =  pygame.transform.rotate(hunter_pic,270)
hunter_pic_L =  pygame.transform.flip(hunter_pic,True,False)
hunter_pic_U =  pygame.transform.rotate(hunter_pic,90)
hunter_pic_R =  hunter_pic

#board = [[]]
board = np.empty(101, dtype=np.object)
for i in range(0,101):
    board[i] = []
    board[i].append(i)

def checkEmpty(list_pos,direction):

    if direction == "X":
        if all ([board[list_pos].count("pit")==0,
             board[list_pos].count("treasure")==0,board[list_pos].count("wumpus")==0]):
            return True
        return False

    if direction == "E":
        if all ([board[list_pos + 1].count("pit")==0, board[list_pos + 1].count("hunter")==0,
             board[list_pos + 1].count("treasure")==0,board[list_pos + 1].count("wumpus")==0]):
            return True
        return False
    if direction == "W":
        if all([board[list_pos - 1].count("pit") == 0, board[list_pos - 1].count("hunter") == 0,
                board[list_pos - 1].count("treasure") == 0, board[list_pos - 1].count("wumpus") == 0]):
            return True
        return False
    if direction == "N":
        if all([board[list_pos - 10].count("pit") == 0, board[list_pos - 10].count("hunter") == 0,
                board[list_pos - 10].count("treasure") == 0, board[list_pos - 10].count("wumpus") == 0]):
            return True
        return False
    if direction == "S":
        if all([board[list_pos + 10].count("pit") == 0, board[list_pos + 10].count("hunter") == 0,
                board[list_pos + 10].count("treasure") == 0, board[list_pos + 10].count("wumpus") == 0]):
            return True
        return False


def setWumpus(screen,wum_pic):
    global wum_pos
    wum_pic = pygame.transform.scale(wum_pic, (58, 58))
    rando_row = random.randint(0, 9)
    rando_col = random.randint(0, 9)

    list_pos = rando_row*10+rando_col
    if list_pos == 90:
        setWumpus(screen,wum_pic)

    else:
        board[list_pos].append(wumpus)
        wum_pos = list_pos
        screen.blit(wum_pic, (((rando_col*60+52),(rando_row*60)+12)))

        if rando_col + 1 < 10:
            board[list_pos + 1].append(stench)
            if checkEmpty(list_pos, "E"):
                pygame.draw.circle(screen, (232, 15, 0), (((rando_col+1)*60+52+12), ((rando_row)*60+12+12)), 10)
        if rando_col - 1 >= 0:
            board[list_pos - 1].append(stench)
            if checkEmpty(list_pos, "W"):
                pygame.draw.circle(screen, (232, 15, 0), (((rando_col - 1) * 60 + 52 + 12), ((rando_row) * 60 + 12 + 12)), 10)
        if rando_row + 1 < 10:
            board[list_pos + 10].append(stench)
            if checkEmpty(list_pos, "S"):
                pygame.draw.circle(screen, (232, 15, 0), (((rando_col) * 60 + 52 + 12), ((rando_row+1) * 60 + 12 + 12)),
                               10)
        if rando_row - 1 >= 0:
            board[list_pos - 10].append(stench)
            if checkEmpty(list_pos, "N"):
                pygame.draw.circle(screen, (232, 15, 0), (((rando_col) * 60 + 52 + 12), ((rando_row-1) * 60 + 12 + 12)),
                               10)

def setPits(screen,pit_pic):
    pit_pic = pygame.transform.scale(pit_pic, (58, 58))
    x=0
    while (x<max_pit):

        rando_row = random.randint(0, 9)
        rando_col = random.randint(0, 9)

        list_pos = rando_row * 10 + rando_col

        if list_pos == 90 or board[list_pos].count("wumpus")>0 or board[list_pos].count("pit")>0 or board[list_pos].count("treasure")>0:
            continue

        else:
            x+=1
            board[list_pos].append(pit)
            screen.blit(pit_pic, (((rando_col * 60 + 52), (rando_row * 60) + 12)))

            if rando_col + 1 < 10 and board[list_pos+1].count("breeze")==0:
                board[list_pos+1].append(breeze)
                if checkEmpty(list_pos,"E"):
                    pygame.draw.circle(screen, (29, 182, 224),
                                   (((rando_col + 1) * 60 + 52 + 28), ((rando_row) * 60 + 12 + 28)), 10)

            if rando_col - 1 >= 0 and board[list_pos-1].count("breeze")==0:
                board[list_pos-1].append(breeze)
                if checkEmpty(list_pos,"W"):
                    pygame.draw.circle(screen, (29, 182, 224),
                                   (((rando_col - 1) * 60 + 52 + 28), ((rando_row) * 60 + 12 + 28)), 10)

            if rando_row + 1 < 10 and board[list_pos+10].count("breeze")==0:
                board[list_pos+10].append(breeze)
                if checkEmpty(list_pos, "S"):
                    pygame.draw.circle(screen, (29, 182, 224),
                                   (((rando_col) * 60 + 52 + 28), ((rando_row+1) * 60 + 12 + 28)), 10)

            if rando_row - 1 >= 0 and board[list_pos-10].count("breeze")==0:
                board[list_pos-10].append(breeze)
                if checkEmpty(list_pos, "N"):
                    pygame.draw.circle(screen, (29, 182, 224),
                                   (((rando_col) * 60 + 52 + 28), ((rando_row-1) * 60 + 12 + 28)), 10)


def setTreasury(screen,treasure_pic):
    treasure_pic = pygame.transform.scale(treasure_pic, (58, 58))
    rando_row = random.randint(0, 9)
    rando_col = random.randint(0, 9)

    list_pos = rando_row * 10 + rando_col

    if list_pos== 90 or board[list_pos].count("wumpus")>0 or board[list_pos].count("pit")>0:
        setTreasury(screen,treasure_pic)
    else:
        board[list_pos].append(treasure)
        screen.blit(treasure_pic, (((rando_col * 60 + 52), (rando_row * 60) + 12)))

        if rando_col + 1 < 10:
            board[list_pos + 1].append(glitter)
            if checkEmpty(list_pos, "E"):
                pygame.draw.circle(screen, (252, 193, 1),
                               (((rando_col + 1) * 60 + 52 + 44), ((rando_row) * 60 + 12 + 44)), 10)

        if rando_col - 1 >= 0:
            board[list_pos - 1].append(glitter)
            if checkEmpty(list_pos, "W"):
                pygame.draw.circle(screen, (252, 193, 1),
                               (((rando_col - 1) * 60 + 52 + 44), ((rando_row) * 60 + 12 + 44)), 10)

        if rando_row + 1 < 10:
            board[list_pos + 10].append(glitter)
            if checkEmpty(list_pos, "S"):
                pygame.draw.circle(screen, (252, 193, 1),
                               (((rando_col) * 60 + 52 + 44), ((rando_row+1) * 60 + 12 + 44)), 10)

        if rando_row - 1 >= 0:
            board[list_pos - 10].append(glitter)
            if checkEmpty(list_pos, "N"):
                pygame.draw.circle(screen, (252, 193, 1),
                               (((rando_col) * 60 + 52 + 44), ((rando_row-1) * 60 + 12 + 44)), 10)

def recreateEnv(screen):
    global wum_pic,pit_pic,treasure_pic
    wum_pic = pygame.transform.scale(wum_pic, (58, 58))
    pit_pic = pygame.transform.scale(pit_pic, (58, 58))
    treasure_pic = pygame.transform.scale(treasure_pic, (58, 58))

    for i in range(0, 100):
            #screen.blit(wum_pic, ((((i%10) * 60 + 52), ((i//10) * 60) + 12)))
        if board[i].count("wumpus")>0:
            screen.blit(wum_pic, ((((i%10) * 60 + 52), ((i//10) * 60) + 12)))
        if board[i].count("treasure") > 0:
            screen.blit(treasure_pic, ((((i%10) * 60 + 52), ((i//10) * 60) + 12)))
        if board[i].count("pit") > 0:
            screen.blit(pit_pic, ((((i%10) * 60 + 52), ((i//10) * 60) + 12)))
        if board[i].count("glitter") > 0 and checkEmpty(i,"X"):
            pygame.draw.circle(screen, (252, 193, 1),
                               (((i%10) * 60 + 52 + 44), ((i//10) * 60 + 12 + 44)), 10)
        if board[i].count("stench") > 0 and checkEmpty(i,"X"):
            pygame.draw.circle(screen, (232, 15, 0), (((i%10) * 60 + 52 + 12), ((i//10) * 60 + 12 + 12)),
                               10)
        if board[i].count("breeze")>0 and checkEmpty(i,"X"):
            pygame.draw.circle(screen, (29, 182, 224),
                               (((i%10) * 60 + 52 + 28), ((i//10) * 60 + 12 + 28)), 10)
        if board[i].count("safe")>0 and checkEmpty(i,"X"):
            pygame.draw.circle(screen, (66, 230, 7),
                               (((i%10) * 60 + 52 + 44), ((i//10) * 60 + 12 + 12)), 10)


def initializeBoard(screen):
    global wum_pic,hunter_pic,pit_pic,treasure_pic
    board[90].append(hunter_pos)
    board[90].append(safe)
    hunter_pic = pygame.transform.scale(hunter_pic, (58, 58))
    screen.blit(hunter_pic, (52, 552))

    setWumpus(screen,wum_pic)
    setTreasury(screen,treasure_pic)
    setPits(screen,pit_pic)

def updateHunter(prev_pos, current_pos, screen):
    global hunter_pic
    if board[prev_pos].count(hunter_pos)>0:
        board[prev_pos].remove(hunter_pos)
    board[current_pos].append(hunter_pos)
    board[current_pos].append(safe)
    hunter_pic = pygame.transform.scale(hunter_pic, (58, 58))
    if prev_pos-current_pos==10:
        hunter_pic = hunter_pic_U
    if prev_pos-current_pos==-1:
        hunter_pic = hunter_pic_L
    if prev_pos-current_pos==1:
        hunter_pic = hunter_pic_R
    if prev_pos-current_pos==-10:
        hunter_pic = hunter_pic_D
    #screen.blit(hunter_pic, (52, 552))
    screen.blit(hunter_pic,((((current_pos%10) * 60 + 52), ((current_pos//10) * 60) + 12)))
    b = checkGameOver(current_pos)
    return b

def checkGameOver(current_pos):
    if any(wp in board[current_pos] for wp in ("wumpus","pit")):
        return "dead"
    if "treasure" in board[current_pos]:
        return "victory"

def wumpus_isDead(screen):
    global wum_pos,wum_pic
    print(wum_pos)
    if wum_pos+1<100 and board[wum_pos+1].count(stench)>0:
        print('ry')
        board[wum_pos+1].remove(stench)
    if wum_pos-1>0 and board[wum_pos-1].count(stench)>0:
        print('ly')
        board[wum_pos-1].remove(stench)
    if wum_pos+10<100 and board[wum_pos+10].count(stench)>0:
        print('dy')
        board[wum_pos+10].remove(stench)
    if wum_pos-10>=0 and board[wum_pos-10].count(stench)>0:
        print('uy')
        board[wum_pos-10].remove(stench)

    wum_pic = wumDead_pic
    screen.blit(wum_pic, ((((wum_pos % 10) * 60 + 52), ((wum_pos // 10) * 60) + 12)))

def doReset():
    global wum_pic,hunter_pic,hunter_pic_R
    wum_pic = pygame.image.load("./UI/assets/wumpus.jpg")
    wum_pic = pygame.transform.scale(wum_pic, (58, 58))
    hunter_pic = hunter_pic_R
    for i in range(0, 101):
        board[i] = []
        board[i].append(i)


