import itertools
import random
from board import show_board, show_start_board

WINNING_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [5, 2, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
GRID = [1, 2, 3, 4, 5, 6, 7, 8, 9]
GAME = True

# Countwinnig combination
def count_comb(my_comb):
    global GAME
    my_possible_comb = itertools.combinations(my_comb, 3)
    for my_comb in my_possible_comb:
        sorted_my_comb = sorted(my_comb)
        for win_comb in WINNING_COMBINATIONS:
            if sorted_my_comb == sorted(win_comb):
                GAME = False
                return GAME

X_player = []
O_player = []
PLAYERS = [X_player, O_player]
X_O = ['X', 'O']

# Choose Auto or manual mode
auto = False
auto_choosing = True
while auto_choosing:
    do_you_want = input('Auto or manualy?(A/M) ').upper()
    if do_you_want == 'M':
        auto = False
        auto_choosing = False
    elif do_you_want == 'A':
        auto = True

        choosing_player = True
        while choosing_player:
            r_player = input('Choose your side (X/O): ').upper()
            if r_player == 'X' or r_player == 'O':
                choosing_player = False
                auto_choosing = False
            else:
                print("Choose 'X' or 'O' ")
    else:
        print('Choose "A" ot "M"?' )

# Show Instructions
show_start_board()

# Auto Game
if auto == True:
    while GAME:
        
        # X Player turn
        show_board(X_player, O_player)
        X_round = True
        while X_round:
            if r_player == 'X':
                try:
                    turn = int(input(f'Player X turn: '))
                    if turn in GRID:
                        X_player.append(turn)
                        GRID.remove(turn)
                        X_round = False
                    else:
                        print("Choose number from 1 to 9.")
                except ValueError:
                    print("Choose number from 1 to 9.")
                count_comb(X_player)
            elif r_player == 'O':
                turn = random.choice(GRID)
                print(f'Player X turn: {turn}')
                X_player.append(turn)
                GRID.remove(turn)
                X_round = False
                count_comb(X_player)

        if GAME == False:
            print(f'\nPlayer X Win!')
            break
        elif GRID == []:
            print(f"\nIt's draw!")
            break

        # O player turn
        show_board(X_player, O_player)
        O_round = True
        while O_round:
            if r_player == 'O':
                try:
                    turn = int(input(f'Player O turn: '))
                    if turn in GRID:
                        O_player.append(turn)
                        GRID.remove(turn)
                        O_round = False
                    else:
                        print("Choose number from 1 to 9.")
                except ValueError:
                    print("Choose number from 1 to 9.")
                count_comb(O_player)
            elif r_player == 'X':
                turn = random.choice(GRID)
                print(f'Player O turn: {turn}')
                O_player.append(turn)
                GRID.remove(turn)
                O_round = False
                count_comb(O_player)

        if GAME == False:
            print(f'\nPlayer O Win!')
            break
        elif GRID == []:
            print(f"\nIt's draw!")
            break

# Manual Game
else:
    while GAME:
        for player in PLAYERS:
            show_board(X_player, O_player)
            round = True
            while round:
                try:
                    turn = int(input(f'Player {X_O[PLAYERS.index(player)]} turn: '))
                    if turn in GRID:
                        player.append(turn)
                        GRID.remove(turn)
                        round = False
                    else:
                        print("Choose number from 1 to 9.")
                except ValueError:
                    print("Choose number from 1 to 9.")
                count_comb(player)
            if GAME == False:
                print(f'\nPlayer {X_O[PLAYERS.index(player)]} Win!')
                break
            elif GRID == []:
                GAME = False
                print(f"\nIt's draw!")
                break

show_board(X_player, O_player)
print("The End!")
