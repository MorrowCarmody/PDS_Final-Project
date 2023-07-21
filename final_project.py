# Matt Carmody
# COSC 6375
# Final Project

import re
import copy

def choose_mark():
    """Allows the player to select their mark and returns an array of form [player_one_mark, player_two_mark]."""
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
        print_game(game)
        print(f'{player} WINS!')
        return True
    # Check for tie
    elif not any(' ' in x for x in game):
        print_game(game)
        print('TIE!')
        return True

def get_move_input(game_state):
    """Returns an array of where the player wants to add their mark of form [column][row]."""
    # Note: I chose the range 1-3 since most users would be unfamiliar with zero-based numbering
    print('Enter a number for the row and a number for the column separated by a comma. (Ex: 1,3)')
    print_game(game_state)
    while(True):
        move = input().replace(' ', '')
        if(re.match('[1-3],[1-3]', move)):
            i = int(move.split(',')[0]) - 1
            j = int(move.split(',')[1]) - 1
            if(game_state[i][j] == ' '):
                return[i, j]
            else:
                print('Invalid selection. The specified space is already taken.')
        else:
            print('Invalid selection. Please enter a number for the row and a number for the column separated by a comma. (Ex: 1,3)')

def make_move(game_state, player):
    """Adds the player's selected move to the game."""
    print(f'\nIt is {player}\'s turn.')
    move = get_move_input(game_state)
    game_state[move[0]][move[1]] = player
    if(check_for_win(game_state, player)):
        print('GAME OVER!')
    elif(player == 'X'):
        make_move(game_state, 'O')
    else:
        make_move(game_state, 'X')

def print_game(game):
    """Prints the current state of the game."""
    print(' ',game[0][0],'|',game[0][1],'|',game[0][2])
    print('-------------')
    print(' ',game[1][0],'|',game[1][1],'|',game[1][2])
    print('-------------')
    print(' ',game[2][0],'|',game[2][1],'|',game[2][2])

def show_example(game):
    print('In this game you will enter a number for the row and a number for the column separated by a comma.')
    print('For example, input "1,3" will result in the following move:')
    game_example = copy.deepcopy(game)
    game_example[0][2] = 'X'
    print_game(game_example)

def play_tic_tac_toe():
    """Starts a game of tic-tac-toe."""
    game_state = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
    print('WELCOME TO TIC-TAC-TOE!')
    show_example(game_state)
    player_marks = choose_mark()
    print(f'Player one has selected {player_marks[0]}, Player two is {player_marks[1]}.')
    make_move(game_state, player_marks[0])

play_tic_tac_toe()
# Add option to continue playing
