from core import *

#TODO: Ability to add level information (Description, picture, answer)
#TODO: Add information about level to file (level count, author)
#TODO: When the editor is open, the following information will be displayed (You logged in as Username, level count, number of level)
#TODO /SUCCESS /D: Menu of editor (create level, show level (enter level number), update level, delete level)
#TODO: In file: level count, number of level, author, description, picture, answer

class Editor:
    def __init__(self):
        self.count = 0
        self.level = 0


    def mainMenu(self, username):
        print('You logged in as', username)
        setLanguage('menuEditor')

        while True:
            userSelect = input('> ')

            if userSelect in menuEditor:
                if userSelect == menuEditor[0] or userSelect == menuEditor[1]:
                    self.createLevel(username)
                elif userSelect == menuEditor[2] or userSelect == menuEditor[3]:
                    self.showLevel()
                elif userSelect == menuEditor[4] or userSelect == menuEditor[5]:
                    self.updateLevel()
                elif userSelect == menuEditor[6] or userSelect == menuEditor[7]:
                    self.deleteLevel()
                elif userSelect == menuEditor[8]:
                    sys.exit()
            else:
                setLanguage('userSelectIncorrect')
                continue


    def createLevel(self, username):
        while True:
            author = username

            self.level = self.count

            setLanguage('descriptionLevel')
            desc = input('> ')

            setLanguage('pictureLevel')
            pic = input('> ')

            setLanguage('answerLevel')
            ans = input('> ')

            self.count = 1

            _mCreateLevel = Model()
            _mCreateLevel.createLevelModel(self.count, self.level, author, desc, pic, ans)

            print('Are you want to exit or continue?')
            print('Press Q for exit or C for continue: ')
            userSelect = input('> ')

            if userSelect == 'C':
                continue
            elif userSelect == 'Q':
                self.mainMenu(username)
            else:
                print('This key is not found')
                continue

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