import numpy as np
import random
player_pos,safe,treasury,pit,wumpus, breeze, glitter, stench, max_pit,board_size = "player","safe","gold","pit","wumpus","breeze","glitter","stench",10,10
arrow = True
#board = [[]]
board = np.empty(100, dtype=np.object)
for i in range(0,100):
    board[i] = []
    board[i].append(i)

def setWumpus():

    rando_row = random.randint(0, 9)
    rando_col = random.randint(0, 9)

    list_pos = rando_row*10+rando_col
    if list_pos == 90:
        setWumpus()

    else:
        board[list_pos].append(wumpus)
        if rando_col + 1 < 10:
            board[list_pos + 1].append(stench)
        if rando_col - 1 >= 0:
            board[list_pos - 1].append(stench)
        if rando_row + 1 < 10:
            board[list_pos + 10].append(stench)
        if rando_row - 1 >= 0:
            board[list_pos - 10].append(stench)

def setPits():

    for x in range(0,max_pit):
        rando_row = random.randint(0, 9)
        rando_col = random.randint(0, 9)

        list_pos = rando_row * 10 + rando_col

        if list_pos == 90 or board[list_pos].count("wumpus")>0 or board[list_pos].count("pit")>0:
            x-=1
        else:
            board[list_pos].append(pit)
            if rando_col + 1 < 10 and board[list_pos+1].count("breeze")==0:
                board[list_pos+1].append(breeze)
            if rando_col - 1 >= 0 and board[list_pos-1].count("breeze")==0:
                board[list_pos-1].append(breeze)
            if rando_row + 1 < 10 and board[list_pos+10].count("breeze")==0:
                board[list_pos+10].append(breeze)
            if rando_row - 1 >= 0 and board[list_pos-10].count("breeze")==0:
                board[list_pos-10].append(breeze)

def setTreasury():
    rando_row = random.randint(0, 9)
    rando_col = random.randint(0, 9)

    list_pos = rando_row * 10 + rando_col

    if list_pos== 90 or board[list_pos].count("wumpus")>0 or board[list_pos].count("pit")>0:
        setTreasury()
    else:
        board[list_pos].append(treasury)
        if rando_col + 1 < 10:
            board[list_pos + 1].append(glitter)
        if rando_col - 1 >= 0:
            board[list_pos - 1].append(glitter)
        if rando_row + 1 < 10:
            board[list_pos + 10].append(glitter)
        if rando_row - 1 >= 0:
            board[list_pos - 10].append(glitter)

def initializeBoard():

    board[90].append(player_pos)

    setWumpus()
    setTreasury()
    setPits()
    print(board)


