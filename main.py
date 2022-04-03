import itertools
from board import show_board, show_start_board

WINNING_COMBINATIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [5, 2, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
GRID = [1, 2, 3, 4, 5, 6, 7, 8, 9]
GAME = True


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
show_start_board()

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
            print(f"\nIt's draw!")
            break

show_board(X_player, O_player)
print("The End!")




