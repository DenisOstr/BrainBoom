from core import *

def getLanguage():
    print('''
        Press E key for set English language
        Press R key for set Russian language
        English (Default)
        ''')

    while True:
        userLang = input('> ')
    
        if userLang == 'E':
            _wConfFile = open('../config.ini', 'w')
            
            _wConfFile.write('selectedLanguage: Eng.')

            _wConfFile.close()
            break
        elif userLang == 'R':
            _wConfFile = open('../config.ini', 'w')
            
            _wConfFile.write('selectedLanguage: Ru.')

            _wConfFile.close()
            break
        elif userLang == '':
            _wConfFile = open('../config.ini', 'w')
            
            _wConfFile.write('selectedLanguage: Eng.')

            _wConfFile.close()
            break
        else:
            print('This language is not found')
            continue


def setLanguage(string):
    _rConfFile = open('../config.ini', 'r')
    _rConfFile = _rConfFile.read()

    fPos = _rConfFile.find('selectedLanguage:')
    sPos = _rConfFile.find(' ', fPos)
    tPos = _rConfFile.find('.', sPos)

    if _rConfFile[sPos+1:tPos] == 'Eng':
        setEng(string)
    elif _rConfFile[sPos+1:tPos] == 'Ru':
        setRu(string)
        

def setEng(string):
    _rEngFile = open('../Locals/eng.loc', 'r')
    _rEngFile = _rEngFile.read()

    fPos = _rEngFile.find(string)
    sPos = _rEngFile.find('>', fPos)
    tPos = _rEngFile.find('!', fPos)

    print('\n', _rEngFile[sPos+1:tPos], '\n')


def setRu(string):
    _rRuFile = open('../Locals/ru.loc', 'r', encoding='utf8')
    _rRuFile = _rRuFile.read()

    fPos = _rRuFile.find(string)
    sPos = _rRuFile.find('>', fPos)
    tPos = _rRuFile.find('!', fPos)

    print('\n', _rRuFile[sPos+1:tPos], '\n')