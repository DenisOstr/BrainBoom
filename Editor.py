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
        print(menuEditorEng)
        # NameError: name 'username' is not defined -> AdminAuth.py username
        #print(userAuthenticationEng, username)

        while True:
            userSelect = input('> ')

            if userSelect in menuEditor:
                if userSelect == menuEditor[0] or menuEditor[1] or menuEditor[2]:
                    self.createLevel(self)
                elif userSelect == menuEditor[3] or menuEditor[4] or menuEditor[5]:
                    self.showLevel(self)
                elif userSelect == menuEditor[6] or menuEditor[7] or menuEditor[8]:
                    self.updateLevel(self)
                elif userSelect == menuEditor[9] or menuEditor[10] or menuEditor[11]:
                    self.deleteLevel(self)
                elif userSelect == menuEditor[12] or menuEditor[13] or menuEditor[14]:
                    run()
            else:
                print(userSelectIncorrect)
                continue


    def createLevel(self):
        print(descriptionLevelEng)
        desc = input('> ')

        print(pictureLevelEng)
        pic = input('> ')

        # there can be several answers to the same level
        # first ask how many answers should be
        print(andwerLevelEng)
        ans = input('>')

        # while True:
        #     i = 0

        #     file(count, i += 1, username, desc, pic, ans)


    def showLevel(self):
        print(enterNumberLevelEng)
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
