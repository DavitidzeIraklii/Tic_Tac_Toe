def show_board(turns_X, turns_O):
    bord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hor = '-----------'

    for n in range(len(bord)):
        for turn in turns_X:
            if turn == bord[n]:
                bord[n] = 'X'
        for turn in turns_O:
            if turn == bord[n]:
                bord[n] = 'O'
        if bord[n] != 'X' and bord[n] != 'O':
            bord[n] = ' '

    print(f'\n {bord[0]} | {bord[1]} | {bord[2]} \n{hor}\n {bord[3]} | {bord[4]} | {bord[5]}\n{hor}\n {bord[6]} | {bord[7]} | {bord[8]}')

def show_start_board():
    bord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hor = '-----------'

    print(f'\n {bord[0]} | {bord[1]} | {bord[2]} \n{hor}\n {bord[3]} | {bord[4]} | {bord[5]}\n{hor}\n {bord[6]} | {bord[7]} | {bord[8]}')
    print(f'Choose one of the numbers to put your symbol')