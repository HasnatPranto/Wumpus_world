"""
Created on: 17/10/2021
@author: Ahmed Ryan
"""

current_hunter_position = None
deg = 0
wumpus_lock = 0
treasure_lock = 0
knowledge_base = {}
visited_cells=[]
HVTSet1 = []
HVTSet2 =[]


def initKB():
    global knowledge_base, deg, current_hunter_position, visited_cells, HVT_lock,HVTSet1, HVTSet2, treasure_lock, wumpus_lock
    current_hunter_position = None
    deg = 0
    treasure_lock = 0
    wumpus_lock = 0
    visited_cells = []
    HVTSet1 = []
    HVTSet2 = []

    knowledge_base = {
        '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
        '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [],
        '20': [], '21': [], '22': [], '23': [], '24': [], '25': [], '26': [], '27': [], '28': [], '29': [],
        '30': [], '31': [], '32': [], '33': [], '34': [], '35': [], '36': [], '37': [], '38': [], '39': [],
        '40': [], '41': [], '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [],
        '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': [], '57': [], '58': [], '59': [],
        '60': [], '61': [], '62': [], '63': [], '64': [], '65': [], '66': [], '67': [], '68': [], '69': [],
        '70': [], '71': [], '72': [], '73': [], '74': [], '75': [], '76': [], '77': [], '78': [], '79': [],
        '80': [], '81': [], '82': [], '83': [], '84': [], '85': [], '86': [], '87': [], '88': [], '89': [],
        '90': [], '91': [], '92': [], '93': [], '94': [], '95': [], '96': [], '97': [], '98': [], '99': [],
    }

# pit, wumpus, gold, visited, safe
'''probable_knowledge_base = {
    '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
    '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [],
    '20': [], '21': [], '22': [], '23': [], '24': [], '25': [], '26': [], '27': [], '28': [], '29': [],
    '30': [], '31': [], '32': [], '33': [], '34': [], '35': [], '36': [], '37': [], '38': [], '39': [],
    '40': [], '41': [], '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [],
    '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': [], '57': [], '58': [], '59': [],
    '60': [], '61': [], '62': [], '63': [], '64': [], '65': [], '66': [], '67': [], '68': [], '69': [],
    '70': [], '71': [], '72': [], '73': [], '74': [], '75': [], '76': [], '77': [], '78': [], '79': [],
    '80': [], '81': [], '82': [], '83': [], '84': [], '85': [], '86': [], '87': [], '88': [], '89': [],
    '90': [], '91': [], '92': [], '93': [], '94': [], '95': [], '96': [], '97': [], '98': [], '99': [],
}'''

# visited cells



def update_knowledge_base_with_current_position_info(info_list):

    global  current_hunter_position# print(info_list)
    global current_hunter_position
    prev_pos = current_hunter_position
    current_hunter_position = str(info_list[0])  # info_list[0] indicates location
    # print(current_hunter_position)

    if knowledge_base[current_hunter_position].count('visited')==0:
        knowledge_base[current_hunter_position] = info_list[1:]
        knowledge_base[current_hunter_position].append('visited')
        if prev_pos != None and knowledge_base[prev_pos].count('hunter')>0:
            knowledge_base[prev_pos].remove('hunter')
        acquireKnowledge()


def adjacent_cells(cell_position):

    cell_position = int(cell_position)
    if (cell_position + 1) < 100 and (cell_position + 1) % 10 != 0:
        right = (cell_position + 1)
    else:
        right = None
    if (cell_position - 1) >= 0 and ((cell_position) - 1) % 10 != 9:
        left = (cell_position) - 1
    else:
        left = None
    lower = (cell_position + 10) if (cell_position + 10) < 100 else None
    upper = (cell_position - 10) if (cell_position) - 10 >= 0 else None


    return {'right': right, 'left': left, 'upper': upper, 'lower': lower}


def acquireKnowledge():

    global current_hunter_position
    # print(knowledge_base[current_hunter_position])
    info = knowledge_base[current_hunter_position]

    if all([info.count("breeze") == 0, info.count("stench") == 0]):

        safe_cells = adjacent_cells(int(current_hunter_position))

        for value in list(safe_cells.values()):
            if value is not None:
                #knowledge_base[str(value)].append('safe')
                if knowledge_base[str(value)].count('safe') == 0:
                    visited_cells.append(str(value))
                    knowledge_base[str(value)].append('safe')

    # mark visited cells
    if knowledge_base[current_hunter_position].count('visited') == 0:
        visited_cells.append(current_hunter_position)
        knowledge_base[current_hunter_position].append('visited')
        if knowledge_base[current_hunter_position].count('safe') == 0:
            knowledge_base[current_hunter_position].append('safe')

    # if stench
    if info.count('stench') > 0:
        probable_wumpus_cells = adjacent_cells(current_hunter_position)
        cells = []
        for value in list(probable_wumpus_cells.values()):
            if value is not None:
                if knowledge_base[str(value)].count('visited')==0:
                    knowledge_base[str(value)].append('wumpus')
                    cells.append(value)
        pinpointHVT(cells, 'wum')

    # if breeze
    if info.count('breeze') > 0:
        probable_pit_cells = adjacent_cells(current_hunter_position)

        for value in list(probable_pit_cells.values()):
            if value is not None:
                if knowledge_base[current_hunter_position].count('pit') == 0:
                    if knowledge_base[str(value)].count('pit') == 0:
                        knowledge_base[str(value)].append('pit')

    # if glitter
    if info.count('glitter') > 0:
        cells = []

        probable_gold_cells = adjacent_cells(current_hunter_position)

        for value in list(probable_gold_cells.values()):
            if value is not None:
                if knowledge_base[str(value)].count('visited')==0:
                    knowledge_base[str(value)].append('treasure')
                    cells.append(value)

        pinpointHVT(cells,'treasure')
    # if visited
    for cell in visited_cells:
        # remove possibility of pit

        if knowledge_base[cell].count('pit')>0 and knowledge_base[cell].count('safe')>0:
            knowledge_base[cell].remove('pit')

        if knowledge_base[cell].count('wumpus')>0 and knowledge_base[cell].count('safe')>0:
            knowledge_base[cell].remove('wumpus')

        '''if probable_knowledge_base[cell].count('pit') > 0:
            probable_knowledge_base[cell].remove('pit')
        # remove possibility of wumpus
        if probable_knowledge_base[cell].count('wumpus') > 0:
            probable_knowledge_base[cell].remove('wumpus')'''

    print(knowledge_base)
    # print status
    '''for key, value in probable_knowledge_base.items():
        if value:
            print(str(key) + ': ' + str(value))'''

    print('#####')
    #print(knowledge_base)

def pinpointHVT(hvtSet,mark):

    global HVTSet1, HVTSet2, treasure_lock,wumpus_lock

    if mark== 'treasure':
        if treasure_lock == 0:
            HVTSet1 = hvtSet
            treasure_lock = 1
        else:
            Set1 = set(HVTSet1)
            Set2 = set(hvtSet)
            treasurePos = Set1.intersection(Set2)
            treasurePos = treasurePos.pop()
            print("treasure", treasurePos)

    if mark== 'wum':
        if wumpus_lock == 0:
            HVTSet2 = hvtSet
            wumpus_lock = 1
        else:
            Set3 = set(HVTSet2)
            Set4 = set(hvtSet)
            wumPos = Set3.intersection(Set4)
            wumPos = wumPos.pop()
            print("wumpus", wumPos)