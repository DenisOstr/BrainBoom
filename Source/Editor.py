from core import *

#TODO: Ability to add level information (Description, picture, answer)
#TODO: Add information about level to file (level count, author)
#TODO: When the editor is open, the following information will be displayed (You logged in as Username, level count, number of level)
#TODO /SUCCESS /D: Menu of editor (create level, show level (enter level number), update level, delete level)
#TODO: In file: level count, number of level, author, description, picture, answer

class Editor:
    def __init__(self):
        _rLevelFile = open(p_levelFile, 'r')
        _rLevelFile = _rLevelFile.read()

        if _rLevelFile == '':
            self.count = 1
        else:
            getLevelsData = []

            _rLevelFile = _rLevelFile.split()

            for _lGetLevels in _rLevelFile:
                if _lGetLevels.startswith('level'):
                    getLevelsData.append(_lGetLevels)

            levels = []
            maxLevel = 0

            for _lLevel in getLevelsData:
                fPos = _lLevel.find('level')
                sPos = _lLevel.find('#', fPos)
                tPos = _lLevel.find('.', sPos)

                levels.append(_lLevel[sPos+1:tPos])

            maxLevel = max(levels)
            maxLevel = int(maxLevel)

            self.count = maxLevel + 1


    def mainMenu(self, username):
        setLanguage('loggedIn', username)
        setLanguage('menuEditor', '')

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
                setLanguage('userSelectIncorrect', '')
                continue


    def createLevel(self, username):
        while True:
            author = username

            level = self.count

            setLanguage('descriptionLevel', '')
            desc = input('> ')

            setLanguage('pictureLevel', '')
            pic = input('> ')

            setLanguage('answerLevel', '')
            ans = input('> ')

            self.count += 1

            _mCreateLevel = Model()
            _mCreateLevel.createLevelModel(level, author, desc, pic, ans)

            setLanguage('wantExitOrContinue', '')
            setLanguage('pressQorC', '')
            userSelect = input('> ')

            if userSelect == 'C':
                continue
            elif userSelect == 'Q':
                self.mainMenu(username)
            else:
                setLanguage('keyNotFound', '')
                self.mainMenu(username)


    def showLevel(self):
        setLanguage('enterNumberLevel', '')
        numberOfLevel = input('> ')

        _mShowLevel = Model()
        _mShowLevel.showLevelModel()

        # firstPos = file.startswith("level:")

        # fPos = file.find(numberOfLevel)
        # res = file[fPos]
        # print('Level #' %s res)


    def updateLevel(self):
        pass


    def deleteLevel(self):
        pass