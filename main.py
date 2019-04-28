"""
    𝐌𝐀𝐃𝐄 𝐁𝐘: 𝙒𝙞𝙡𝙡𝙞𝙖𝙣 𝙎𝙖𝙡𝙘𝙚𝙙𝙖
    𝐕𝐄𝐑𝐒𝐈𝐎𝐍: 𝟎.𝟏
    𝐃𝐀𝐓𝐄: 𝟐𝟏/𝐀𝐩𝐫𝐢𝐥/𝟐𝟎𝟏𝟗
"""

"""
    IDEA FOR AFTER THE PROGRAM IS DONE:
    CREATE A <CLASS> THAT WILL HAVE <DEF's> THAT HANDLE ALL THE TRY AND EXCEPT IN UOR PROGRAM
"""


from time import sleep

import msvcrt as m # Using it for 'Press any key to continue' thing.

import os
import keyboard

class TicTacToe:
    def __init__(self):
        self.difficultAI = 1
        self.playWith = 3  # 3 = Strings and Numbers
    def menuSelection(self):
        os.system('cls')

        print(f'[1] - Play\n'
              f'[2] - Options\n'
              f'[3] - Exit')

        try:
            option = int(input('I\'ll go with '))
        except ValueError as valueError:
            print(f'Invalid Option\n'
                  f'Following error: {valueError}\n'
                  f'Press any key to continue...')

            m.getch() # Waiting for any key to be pressed.min
            os.system('cls')
            objectRun.menuSelection() # Call menuSelection again.


        if option == 1:
            objectRun.play()
        elif option == 2:
            pass
        elif option == 3:
            exit()
        else:
            print(f'You should choose something between 1 and 3, and not {option}'
                  f'Press any key to continue...')

            m.getch()
            objectRun.menuSelection()
             
    def drawBoard(self, topL='?', topM='!', topR='?',
                        midL='!', midM='?', midR='!',
                        lowL='?', lowM='!', lowR='?',):
        board = {
            'top-L': topL,
            'top-M': topM,
            'top-R': topR,

            'mid-L': midL,
            'mid-M': midM,
            'mid-R': midR,

            'low-L': lowL,
            'low-M': lowM,
            'low-R': lowR,
        }

        print(' {0} | {1} | {2}\n'
              '----------\n'
              ' {3} | {4} | {5}\n'
              '----------\n'
              ' {6} | {7} | {8}\n'.format(board['top-L'], board['top-M'], board['top-R'],
                                     board['mid-L'], board['mid-M'], board['mid-R'],
                                     board['low-L'], board['low-M'], board['low-R']))

    # change that stupid name when done
    def play(self):
        os.system('cls')

        print(f'[1] - Player VS Player\n'
              f'[2] - Player VS Machine\n'
              f'[3] - Return')

        try:
            option = int(input('I\'ll go with '))
        except ValueError as valueError:
            print(f'Invalid Option\n'
                  f'Following error: {valueError}\n'
                  f'Press any key to continue...')
            m.getch()
            objectRun.play()

        try:
            if option == 1:
                os.system('cls')

                self.drawBoard()
                if self.playWith == 1:  # Numbers
                    print('Player 1, it\'s your turn\n'
                          'You can choose between 1 (TOP LEFT) up to 9 (BOTTOM RIGHT)')

                    playerOne = int('I\'ll go with ')
        
                elif self.playWith == 2:  # Strings
                    pass
                else:  # Strings and Numbers
                    pass
            elif option == 2:
                pass
            elif option == 3:
                objectRun.menuSelection()
            else:
                print(f'You should choose something between 1 and 3, and not {option}'
                      f'Press any key to continue...')

                m.getch()
                objectRun.play()

        except:
            print('ERROR AT LINE 85, GO FIND WHAT IS WRONG')

    def playerOptions(self):
        if playerOne == 1:
            os.system('cls')
            drawBoard(topL='X')
        elif playerOne == 2:
            os.system('cls')
            drawBoard(topM='X')
        elif playerOne == 3:
            os.system('cls')
            drawBoard(topR='X')
        elif playerOne == 4:
            os.system('cls')
            drawBoard(midL='X')
        elif playerOne == 5:
            os.system('cls')
            drawBoard(midM='X')
        elif playerOne == 6:
            os.system('cls')
            drawBoard(midR='X')
        elif playerOne == 7:
            os.system('cls')
            drawBoard(lowL='X')
        elif playerOne == 8:
            os.system('cls')
            drawBoard(lowM='X')
        elif playerOne == 9:
            os.system('cls')
            drawBoard(lowR='X')
        else:
            pass

    def options(self):
        os.system('cls')

        print(f'[1] - Difficult\n'
              f'[2] - P\n'
              f'[3] - Exit')

        try:
            option = int(input('I\'ll go with '))
        except ValueError as valueError:
            print(f'You should choose something between 1 and 3, and not {option}'
                  f'Press any key to continue...')

            m.getch()
            objectRun.menuSelection()
              

        self.difficultAI = int(input('[1] - EASY\n'
                                '[2] - MEDIUM\n'
                                '[3] - HARD\n'
                                'I\'ll go with '))

        self.playWith = int(input('[1] - NUMBERS\n'
                                '[2] - STRING\n'
                                '[3] - BOTH\n'
                                'I\'ll go with '))


if __name__ == '__main__':
    objectRun = TicTacToe()

    objectRun.menuSelection()