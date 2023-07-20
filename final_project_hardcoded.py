# Matt Carmody
# COSC 6375
# Final Project

game = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]

def choose_mark():
    # return array with p1 in [0] and p2 in [1]
    choosing = True
    print('Would you like to play as X or O?')
    while(choosing):
        choice = input().lower()
        if(choice == 'x'):
            choosing = False
            print('Player 1 has selected . Player 2 is O.')
            return 'X'
        if(choice == 'o'):
            choosing = False
            print('Player 1 has selected O. Player 2 is X.')
            return 'O'
        else:
            print('Error: Invalid selection. Please select either X or O.')

def reset_game():
    return [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
    
def check_for_win():
    if(game[0][0] == game[0][1] == game[0][2] or # horizontal
       game[1][0] == game[1][1] == game[1][2] or # horizontal
       game[2][0] == game[2][1] == game[2][2] or # horizontal
       game[0][0] == game[1][0] == game[2][0] or # vertical
       game[0][1] == game[1][1] == game[2][1] or # vertical
       game[0][3] == game[1][3] == game[2][3] or # vertical
       game[0][0] == game[1][1] == game[2][2] or # diagonal
       game[0][2] == game[1][1] == game[2][0]):  # diagonal
        return True
    
player_one_var = choose_mark()