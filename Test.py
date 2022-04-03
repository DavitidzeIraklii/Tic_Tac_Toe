import sys

row1 = ["☐", "☐", "☐"]
row2 = ["☐", "☐", "☐"]
row3 = ["☐", "☐", "☐"]
game_running = True
player1_moves = []
player2_moves = []
winning_moves = [["11", "12", "13"], ["21", "22", "23"], ["31", "32", "33"], ["11", "21", "31"], ["12", "22", "32"], ["13", "23", "33"], ["11", "22", "33"], ["31", "22", "13"]]

grid_layout = [row1, row2, row3]
grid = f"{row1}\n{row2}\n{row3}"
print(grid)
while game_running:
    mark_choice = input("Player 1: Choose X or O: ").upper()
    if mark_choice.lower() == "x":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"
    position = input(f"Player 1: Place a {mark_choice}. Type a two digit number(eg.23), 2 means 2nd row, 3 means 3rd column. ")

    def place_mark(mark_to_use, pos):
        try:
            position_row = int(pos[0])
            position_column = int(pos[1])
            grid_layout[position_row - 1][position_column - 1] = mark_to_use
            grid = f"{row1}\n{row2}\n{row3}"
            print(grid)
        except IndexError:
            print("Invalid choice, next player plays. Remember, first digit is for the row, second one for the column")

    place_mark(mark_choice, position)
    player1_moves.append(position)
    for round_nr in range(1, 9):
        if round_nr % 2 == 0:
            current_player = "Player 1"
            mark = player1
        else:
            current_player = "Player 2"
            mark = player2
        def next_move():
            position = input(f"{current_player}: Place an {mark}: ")
            if grid_layout[int(position[0]) - 1][int(position[1]) - 1] != "☐":
                print("You can't place it there, the spot's already taken. Try again.")
                next_move()
            else:
                place_mark(mark, position)
                if mark == player1:
                    player1_moves.append(position)
                else:
                    player2_moves.append(position)
        next_move()
        for win_set in winning_moves:
            if win_set[0] in player1_moves and win_set[1] in player1_moves and win_set[2] in player1_moves:
                print("Player 1 wins! Game over.")
                sys.exit()
            elif win_set[0] in player2_moves and win_set[1] in player2_moves and win_set[2] in player2_moves:
                print("Player 1 wins! Game over.")
                sys.exit()

    print("Draw.")
    sys.exit()