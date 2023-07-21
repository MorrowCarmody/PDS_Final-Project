# Matt Carmody
# COSC 6375
# Final Project

import re
import copy

class TicTacToe:
    game_state = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]

    def __choose_mark():
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
    def __check_for_win(self, player):
        """Determines if a player has won the game."""
        g = self.game_state
        if(g[0][0] != ' ' and g[0][0] == g[0][1] == g[0][2] or # horizontal
        g[1][0] != ' ' and g[1][0] == g[1][1] == g[1][2] or # horizontal
        g[2][0] != ' ' and g[2][0] == g[2][1] == g[2][2] or # horizontal
        g[0][0] != ' ' and g[0][0] == g[1][0] == g[2][0] or # vertical
        g[0][1] != ' ' and g[0][1] == g[1][1] == g[2][1] or # vertical
        g[0][2] != ' ' and g[0][2] == g[1][2] == g[2][2] or # vertical
        g[0][0] != ' ' and g[0][0] == g[1][1] == g[2][2] or # diagonal
        g[0][2] != ' ' and g[0][2] == g[1][1] == g[2][0]):  # diagonal
            self.__print_game(self.game_state)
            print(f'{player} WINS!')
            return True
        # Check for tie
        elif not any(' ' in x for x in g):
            self.__print_game(self.game_state)
            print('TIE!')
            return True

    def __get_move_input(self):
        """Returns an array of where the player wants to add their mark of form [column][row]."""
        # Note: I chose the range 1-3 since most users would be unfamiliar with zero-based numbering
        # print('Enter a number for the row and a number for the column separated by a comma. (Ex: 1,3)')
        self.__print_game(self.game_state)
        while(True):
            move = input().replace(' ', '')
            if(re.match('[1-3],[1-3]', move)):
                i = int(move.split(',')[0]) - 1
                j = int(move.split(',')[1]) - 1
                if(self.game_state[i][j] == ' '):
                    return[i, j]
                else:
                    print('Invalid selection. The specified space is already taken.')
            else:
                print('Invalid selection. Please enter a number for the row and a number for the column separated by a comma. (Ex: 1,3)')

    def __make_move(self, player):
        """Adds the player's selected move to the game."""
        print(f'\nIt is {player}\'s turn.')
        move = self.__get_move_input(self)
        self.game_state[move[0]][move[1]] = player
        if(self.__check_for_win(self, player)):
            print('GAME OVER!')
            print('Would you like to play again? (y/n)')
            while(True):
                answer = input().lower()
                if(answer == 'y'):
                    self.__reset_game(self)
                    self.play_game()
                    break
                elif(answer == 'n'):
                    print('Thank you for playing!')
                    break
                else:
                    print('Invalid selection. Please enter either "y" or "n".')
        elif(player == 'X'):
            self.__make_move(self, 'O')
        else:
            self.__make_move(self, 'X')

    def __print_game(game_state):
        """Prints the current state of the game."""
        g = game_state
        print(' ',g[0][0],'|',g[0][1],'|',g[0][2])
        print('-------------')
        print(' ',g[1][0],'|',g[1][1],'|',g[1][2])
        print('-------------')
        print(' ',g[2][0],'|',g[2][1],'|',g[2][2])

    def __show_example(self):
        print('In this game you will enter a number for the row and a number for the column separated by a comma.')
        print('For example, input "1,3" will result in the following move:')
        game_example = copy.deepcopy(self.game_state)
        game_example[0][2] = 'X'
        self.__print_game(game_example)
    
    def __reset_game(self):
        for i in range(len(self.game_state)):
            for j in range(len(self.game_state[i])):
                self.game_state[i][j] = ' '

    @classmethod
    def play_game(self):
        """Starts a game of tic-tac-toe."""
        print('WELCOME TO TIC-TAC-TOE!')
        self.__show_example(self)
        player_marks = self.__choose_mark()
        print(f'Player one has selected {player_marks[0]}, Player two is {player_marks[1]}.')
        self.__make_move(self, player_marks[0])