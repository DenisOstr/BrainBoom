from core import *

class Model:
    def __init__(self):
        pass


    def createLevelModel(self, count, level, author, desc, pic, ans):
        _rLevelFile = open('../level.ini', 'r')
        _rLevelFile = _rLevelFile.read()

        fPos = _rLevelFile.find('levelCount:')
        sPos = _rLevelFile.find(' ', fPos)
        tPos = _rLevelFile.find('.', sPos)

        levelCount = int(_rLevelFile[sPos+1:tPos])
        levelCount += count

        if levelCount is not '':
            _wLevelFile = open('../level.ini', 'w')
            
            _wLevelFile.write('levelCount: %s.' % levelCount)

            _wLevelFile.close()

        # _wLevelFile = open('../level.ini', 'a+')
        
        # _wLevelString = '\n\n' + 'Level: %s' % level
        # _wLevelFile.write(_wLevelString)

        # _wLevelFile.close()