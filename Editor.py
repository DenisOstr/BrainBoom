from core import *

#TODO: Ability to add level information (Description, picture, answer)
#TODO: Add information about level to file (level count, author)
#TODO: When the editor is open, the following information will be displayed (You logged in as Username, level count, number of level)
#TODO #SUCCESS: Menu of editor (create level, show level (enter level number), update level, delete level)
#TODO: In file: level count, number of level, author, description, picture, answer

class Editor():
    def __init__(self):
        pass


    def mainMenu(self):
        print('Welcome to the Editor')
        print('''
            1) Press C key for create level
            2) Press S key for show levels
            3) Press U key for update level
            4) Press D key for delete level
            5) Press Backspace for back to main game menu
        ''')

        while True:
            userSelect = input('> ')

            if userSelect == 'C':
                self.createLevel(self)
            elif userSelect == 'S':
                self.showLevel(self)
            elif userSelect == 'U':
                self.updateLevel(self)
            elif userSelect == 'D':
                self.deleteLevel(self)
            elif userSelect == 'Backspace':
                run()
            else:
                print('This key is not found')
                continue


    def createLevel(self):
        print('Enter the description of level: ')
        desc = input('> ')

        print('Enter the picture of level: ')
        pic = input('> ')

        print('Enter the answer of level: ')
        ans = input('> ')

        # while True:
        #     i = 0

        #     file(count, i += 1, username, desc, pic, ans)


    def showLevel(self):
        print('Enter the number of level: ')
        numberOfLevel = input('> ')

        # firstPos = file.startswith("level:")

        # fPos = file.find(numberOfLevel)
        # res = file[fPos]
        # print('Level #' %s res)


    def updateLevel(self):
        pass


    def deleteLevel(self):
        pass


# levelCount = 5

# level: 1
# author: Denis
# description: ...
# picture: ...
# answer: ...

# level: 2
# author: Nikita
# description: ...
# picture: ...
# answer: ...

# level: 3
# author: Nikita
# description: ...
# picture: ...
# answer: ...

# 1
# Nikita
# ...
# ..
# .