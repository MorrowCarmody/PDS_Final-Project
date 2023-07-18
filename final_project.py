# Matt Carmody
# COSC 6375
# Final Project

gb = [[' ' for x in range(3)] for y in range(3)]

# gb = [['1','2','3'],
#       ['4','5','6'],
#       ['7','8','9']]
# gb = [[' ',' ',' '],
#         [' ',' ',' '],
#         [' ',' ',' ']]

def resetGame(arr):
    for i in arr:
        for j in i:
            j = ' '

print(gb)
resetGame(gb)
print(gb)
    
# TODO: Refactor this
def check_gb():
    if(gb[0][0] == gb[0][1] == gb[0][2] or # horizontal
       gb[1][0] == gb[1][1] == gb[1][2] or # horizontal
       gb[2][0] == gb[2][1] == gb[2][2] or # horizontal
       gb[0][0] == gb[1][0] == gb[2][0] or # vertical
       gb[0][1] == gb[1][1] == gb[2][1] or # vertical
       gb[0][3] == gb[1][3] == gb[2][3] or # vertical
       gb[0][0] == gb[1][1] == gb[2][2] or # diagonal
       gb[0][2] == gb[1][1] == gb[2][0]):  # diagonal
        print("GAME OVER!")
    
def playGame():
    finished = False
    while(finished == False):
          print("not finished")
          finished = True
    # show board
    # get user input
    # choose X or O
    # loop: while(running)
        # choose move
        # change players
        # if game finishes, end and announce winner
          

def printGame(arr):
    for i in arr:
        for j in i:
            print(j,' ', end=' ')
        print('\n')
    # HARDCODE BOARD?
    # print(' ',gb[0][0],'|',gb[0][1],'|',gb[0][2])
    # print('-------------')
    # print(' ',gb[1][0],'|',gb[1][1],'|',gb[1][2])
    # print('-------------')
    # print(' ',gb[2][0],'|',gb[2][1],'|',gb[2][2])

printGame(gb)

"""
(Project: Two-Player, Two-Dimensional Tic-Tac-Toe) Write a script to play two-
dimensional Tic-Tac-Toe between two human players who alternate entering their moves
on the same computer. Use a 3-by-3 two-dimensional array. Each player indicates their
moves by entering a pair of numbers representing the row and column indices of the
square in which they want to place their mark, either an 'X' or an 'O'. When the first play-
er moves, place an 'X' in the specified square. When the second player moves, place an
'O' in the specified square. Each move must be to an empty square. After each move, de-
termine whether the game has been won and whether it’s a draw.
"""


"""
In this project, you can choose/design any real world application or data analysis using Python
programming.
Alternatively, you can choose one problem from the exercises in Chapter 4 or any chapter after Chapter 4
of the textbook. This textbook has a rich collection of programming exercises, with varying complexities
and difficulties. Many problems have labels like
Challenge
Project
Challenge Project
Super Challenge Project
Research
Performance Analysis
Intro to Data Science
AI Project
etc.
You can pick any problem. Make sure you choose a project that is challenging enough for your intelligence
capacity but also simple enough for the short period of a summer course

What to Submit:
(1) A Project Report
If you are to choose/design your own application, you need to describe your problems and solutions in
detail. If you are to choose one in the textbook, you need to copy the problem description, and where the
problem is located (chapter, problem number and page number).
(2) The Code
(i)The Jupyter Notebook files (.ijpnb) files, if any. It is alright if you do not use Jupyter Notebook.
(ii) The Python script files.
Do not zip the files. Submit these files separately.
"""


"""
6.8 (Challenge: Writing the Word Equivalent of a Check Amount) In check-writing
systems, it’s crucial to prevent alteration of check amounts. One common security method
requires that the amount be written in numbers and spelled out in words as well. Even if
someone can alter the numerical amount of the check, it’s tough to change the amount in
words. Create a dictionary that maps numbers to their corresponding word equivalents.
Write a script that inputs a numeric check amount that’s less than 1000 and uses the dic-
tionary to write the word equivalent of the amount. For example, the amount 112.43
should be written as
ONE HUNDRED TWELVE AND 43/100
"""
