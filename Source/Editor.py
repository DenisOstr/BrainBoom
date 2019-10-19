from core import *

#TODO: Ability to add level information (Description, picture, answer)
#TODO: Add information about level to file (level count, author)
#TODO: When the editor is open, the following information will be displayed (You logged in as Username, level count, number of level)
#TODO /SUCCESS /D: Menu of editor (create level, show level (enter level number), update level, delete level)
#TODO: In file: level count, number of level, author, description, picture, answer

class Editor():
    def __init__(self):
        pass


    def mainMenu(self):
        setLanguage('menuEditor')

        while True:
            userSelect = input('> ')

            if userSelect in menuEditor:
                if userSelect == menuEditor[0] or userSelect == menuEditor[1]:
                    self.createLevel(self)
                elif userSelect == menuEditor[2] or userSelect == menuEditor[3]:
                    self.showLevel(self)
                elif userSelect == menuEditor[4] or userSelect == menuEditor[5]:
                    self.updateLevel(self)
                elif userSelect == menuEditor[6] or userSelect == menuEditor[7]:
                    self.deleteLevel(self)
                elif userSelect == menuEditor[8]:
                    sys.exit()
            else:
                setLanguage('userSelectIncorrect')
                continue


    def createLevel(self):
        setLanguage('descriptionLevel')
        desc = input('> ')

        setLanguage('pictureLevel')
        pic = input('> ')

        setLanguage('answerLevel')
        ans = input('> ')

        # while True:
        #     i = 0

        #     file(count, i += 1, username, desc, pic, ans)


    def showLevel(self):
        setLanguage('enterNumberLevel')
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
