# Matt Carmody
# COSC 6375
# Final Project

import re

def choose_mark():
    choosing = True
    print('Would you like to play as X or O?')
    while(choosing):
        choice = input().lower()
        if(choice == 'x'):
            choosing = False
            return ['X','O']
        if(choice == 'o'):
            choosing = False
            return ['O','X']
        else:
            print('Invalid selection. Please select either X or O.')
    
def check_for_win(game):
    # TODO: check that the spaces aren't blank
    if(game[0][0] == game[0][1] == game[0][2] or # horizontal
       game[1][0] == game[1][1] == game[1][2] or # horizontal
       game[2][0] == game[2][1] == game[2][2] or # horizontal
       game[0][0] == game[1][0] == game[2][0] or # vertical
       game[0][1] == game[1][1] == game[2][1] or # vertical
       game[0][2] == game[1][2] == game[2][2] or # vertical
       game[0][0] == game[1][1] == game[2][2] or # diagonal
       game[0][2] == game[1][1] == game[2][0]):  # diagonal
        print('GAME OVER!')
        return True

def get_move():
    # Note: I chose the range 1-3 since most users would be unfamiliar with zero-based numbering
    print('Enter a number (1-3) for the column and a number (1-3) for the row separated by a comma.')
    while(True):
        move = input()
        if(re.match('[1-3],[1-3]', move)):
            break
        print('Invalid selection. Please enter a number (1-3) for the column and a number (1-3) for the row separated by a comma.')
    return move

def make_move(game, player):
    choosing = True
    print(f'It is {player}\'s turn.')
    while(choosing):
        move = get_move()
        i = int(move.split(',')[0]) - 1
        j = int(move.split(',')[1]) - 1
        if(game[i][j] == ' '):
            choosing = False
            game[i][j] = player
            print(game)
            check_for_win(game)
            if(player == 'X'):
                make_move(game, 'O')
            else:
                make_move(game, 'X')
        else:
            print('Invalid selection. The specified space is already taken.')

make_move([[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']], 'X')

def print_game(game):
    print(' ',game[0][0],'|',game[0][1],'|',game[0][2])
    print('-------------')
    print(' ',game[1][0],'|',game[1][1],'|',game[1][2])
    print('-------------')
    print(' ',game[2][0],'|',game[2][1],'|',game[2][2])

def reset_game():
    return [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]


def play_game():
    game = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
    player_marks = choose_mark()
    player_one_var = player_marks[0]
    player_two_var = player_marks[1]
    print(f'Player one has selected {player_one_var}, Player two is {player_two_var}.')
    game = make_move(game, player_one_var)
    print_game(game)


# play_game()