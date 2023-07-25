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

    def __check_for_win(self, player):
        """Determines if a player has won the game."""
        gs = self.game_state
        if(gs[0][0] != ' ' and gs[0][0] == gs[0][1] == gs[0][2] or # row 1
           gs[1][0] != ' ' and gs[1][0] == gs[1][1] == gs[1][2] or # row 2
           gs[2][0] != ' ' and gs[2][0] == gs[2][1] == gs[2][2] or # row 3
           gs[0][0] != ' ' and gs[0][0] == gs[1][0] == gs[2][0] or # column 1
           gs[0][1] != ' ' and gs[0][1] == gs[1][1] == gs[2][1] or # column 2
           gs[0][2] != ' ' and gs[0][2] == gs[1][2] == gs[2][2] or # column 3
           gs[0][0] != ' ' and gs[0][0] == gs[1][1] == gs[2][2] or # diagonal
           gs[0][2] != ' ' and gs[0][2] == gs[1][1] == gs[2][0]):  # diagonal
            self.__print_game(self.game_state)
            print(f'{player} WINS!')
            return True
        # Check for tie
        if not any(' ' in x for x in gs):
            self.__print_game(self.game_state)
            print('TIE!')
            return True

    def __get_move_input(self):
        """Returns an array of where the player wants to add their mark of form [column][row]."""
        # Note: I chose the range 1-3 since most users would be unfamiliar with zero-based numbering
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
        print(f'\nIt is {player}\'s turn. Please enter your move:')
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
        gs = game_state
        print(' ',gs[0][0],'|',gs[0][1],'|',gs[0][2])
        print('-------------')
        print(' ',gs[1][0],'|',gs[1][1],'|',gs[1][2])
        print('-------------')
        print(' ',gs[2][0],'|',gs[2][1],'|',gs[2][2])

    def __show_example(self):
        """Prints an example for the user"""
        print('In this game you will enter a number for the row and a number for the column separated by a comma.')
        print('For example, input "1,3" will result in the following move:')
        game_example = copy.deepcopy(self.game_state)
        game_example[0][2] = 'X'
        self.__print_game(game_example)
    
    def __reset_game(self):
        """Resets the state of the game"""
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