from core import *

class Model:
    def __init__(self):
        pass


    def createLevelModel(self, level, author, desc, pic, ans):
        if level is not '':
            _wLevelFile = open(p_levelFile, 'a')
            
            _wLevelString = 'level:#%s.' % level + '\n' + 'author: %s.' % author +\
                '\n' + 'description: %s.' % desc + '\n' + 'picture: %s.' % pic + '\n' + 'answer: %s.' % ans + '\n\n'
            _wLevelFile.write(_wLevelString)

            _wLevelFile.close()


    def showLevelModel(self):
        pass