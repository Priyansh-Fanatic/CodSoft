from math import inf as infinity
import platform
from random import choice
from os import system
import time



Human = -1
Ai = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def empty_cells(s):
    cells = []

    for x, row in enumerate(s):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False
    
def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False
    
def evaluate(s):

    if wins(s, Ai):
        score = +1
    elif wins(s, Human):
        score = -1
    else:
        score = 0

    return score
    
def wins(s, player):

    win_s = [
        [s[0][0], s[0][1], s[0][2]],[s[1][0], s[1][1], s[1][2]],[s[2][0], s[2][1], s[2][2]],[s[0][0], s[1][0], s[2][0]],
        [s[0][1], s[1][1], s[2][1]],[s[0][2], s[1][2], s[2][2]],[s[0][0], s[1][1], s[2][2]],[s[2][0], s[1][1], s[0][2]],
    ]
    if [player, player, player] in win_s:
        return True
    else:
        return False
    
def game_over(s):

    return wins(s, Human) or wins(s, Ai)
    
    
def minimax(s, depth, player):
    if player == Ai:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(s):
        score = evaluate(s)
        return [-1, -1, score]

    for cell in empty_cells(s):
        x, y = cell[0], cell[1]
        s[x][y] = player
        score = minimax(s, depth - 1, -player)
        s[x][y] = 0
        score[0], score[1] = x, y

        if player == Ai:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')
        
def render(s, Ai_ch, human_ch):

    chars = {
        -1: human_ch,
        +1: Ai_ch,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in s:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)
        
def ai_turn(Ai_ch, human_ch):

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{Ai_ch}]')
    render(board, Ai_ch, human_ch)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, Ai)
        x, y = move[0], move[1]

    set_move(x, y, Ai)
    time.sleep(1)
    
def human_turn(Ai_ch, human_ch):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{human_ch}]')
    render(board, Ai_ch, human_ch)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], Human)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    
    
#main
human_ch = ''  # X or O
Ai_ch = ''  # X or O
first = '' 
print("Welcome to tic tac toe!!!!")

while human_ch != 'O' and human_ch != 'X':
    try:
        print('')
        human_ch = input('Choose X or O\nChosen: ').upper()
    except (EOFError, KeyboardInterrupt):
        print('\nError')
        exit()
    except (KeyError, ValueError):
        print('Bad choice')
        
if human_ch== 'X':
    Ai_ch = 'O'
else:
    Ai_ch = 'X'
    
while first != 'Y' and first != 'N':
    try:
        first = input('\nFirst to start?[y/n]: ').upper()
    except (EOFError, KeyboardInterrupt):
        exit()
    except (KeyError, ValueError):
        print('Bad choice')
        
while len(empty_cells(board)) > 0 and not game_over(board):
    if first == 'N':
        ai_turn(Ai_ch, human_ch)
        first = ''

    human_turn(Ai_ch, human_ch)
    ai_turn(Ai_ch, human_ch)
    
if wins(board, Human):
    clean()
    print(f'Human turn [{human_ch}]')
    render(board, Ai_ch, human_ch)
    print('YOU WIN!')
elif wins(board, Ai):
    clean()
    print(f'Computer turn [{Ai_ch}]')
    render(board, Ai_ch, human_ch)
    print('AI WON!!')
else:
    clean()
    render(board, Ai_ch, human_ch)
    print('DRAW!')

exit()


