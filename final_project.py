# Matt Carmody
# COSC 6375
# Final Project

import re

def choose_mark():
    """Allows the player to select X or O to play as."""
    print('Would you like to play as X or O?')
    while(True):
        choice = input().lower().replace(' ', '')
        if(choice == 'x'):
            return ['X','O']
        if(choice == 'o'):
            return ['O','X']
        else:
            print('Invalid selection. Please select either X or O.')

# TODO: Refactor this
def check_for_win(game, player):
    """Determines if a player has won the game."""
    if(game[0][0] != ' ' and game[0][0] == game[0][1] == game[0][2] or # horizontal
       game[1][0] != ' ' and game[1][0] == game[1][1] == game[1][2] or # horizontal
       game[2][0] != ' ' and game[2][0] == game[2][1] == game[2][2] or # horizontal
       game[0][0] != ' ' and game[0][0] == game[1][0] == game[2][0] or # vertical
       game[0][1] != ' ' and game[0][1] == game[1][1] == game[2][1] or # vertical
       game[0][2] != ' ' and game[0][2] == game[1][2] == game[2][2] or # vertical
       game[0][0] != ' ' and game[0][0] == game[1][1] == game[2][2] or # diagonal
       game[0][2] != ' ' and game[0][2] == game[1][1] == game[2][0]):  # diagonal
        print(f'{player} WINS!')
        return True
    # Check for tie
    elif not any(' ' in x for x in game):
        print('TIE!')
        return True

def get_move_input():
    """Allows the player to select the space they want to move."""
    # Note: I chose the range 1-3 since most users would be unfamiliar with zero-based numbering
    print('Enter a number (1-3) for the column and a number (1-3) for the row separated by a comma.')
    while(True):
        move = input().replace(' ', '')
        if(re.match('[1-3],[1-3]', move)):
            # convert to array of zero-based integers
            return [int(move.split(',')[0]) - 1, int(move.split(',')[1]) - 1]
        print('Invalid selection. Please enter a number (1-3) for the column and a number (1-3) for the row separated by a comma.')

def make_move(game, player):
    """Adds the player's selected move to the game."""
    print(f'\nIt is {player}\'s turn.')
    while(True):
        move = get_move_input()
        i = move[0]
        j = move[1]
        if(game[i][j] == ' '):
            game[i][j] = player
            print_game(game)
            if(check_for_win(game, player)):
                print('GAME OVER!')
            elif(player == 'X'):
                make_move(game, 'O')
            else:
                make_move(game, 'X')
            break
        else:
            print('Invalid selection. The specified space is already taken.')

def print_game(game):
    """Prints the current state of the game."""
    print(' ',game[0][0],'|',game[0][1],'|',game[0][2])
    print('-------------')
    print(' ',game[1][0],'|',game[1][1],'|',game[1][2])
    print('-------------')
    print(' ',game[2][0],'|',game[2][1],'|',game[2][2])

def play_tic_tac_toe():
    """Starts a game of tic-tac-toe."""
    game = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
    player_marks = choose_mark()
    player_one_var = player_marks[0]
    player_two_var = player_marks[1]
    print(f'Player one has selected {player_one_var}, Player two is {player_two_var}.')
    game = make_move(game, player_one_var)

play_tic_tac_toe()
