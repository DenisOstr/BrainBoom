#!/usr/bin/env python3
import sys, random
from core import *

#TODO: set language
#TODO: loop
#TODO: update
#TODO: render

def languageSelection():
    print(gameLanguage)
    print(languageList)

    while True:
        lang = input('\n> ')

        if lang == settingLanguage[0] or lang == settingLanguage[1] or lang == settingLanguage[2] or lang == settingLanguage[3]:
            global menuScreen
            menuScreen = '''\nSelect:
    1) Press S key for Start the game
    2) Press Q key for Quit from the game
    3) Press X key for Settings from the game'''

            global menuSelectNotExists
            menuSelectNotExists = 'This function does not exists'

            global gameSettingsTitle
            gameSettingsTitle = '''\nGame settings
    0) Press Z, to go back
    1) Press L, to change the language of the game'''

            break


        elif lang == settingLanguage[4] or lang == settingLanguage[5] or lang == settingLanguage[6] or lang == settingLanguage[7]:

            menuScreen = '''\nВыберите:
    1) Нажмите клавишу S, чтобы начать игру
    2) Нажмите клавишу Q, чтобы выйти
    3) Нажмите клавишу X, чтобы открыть настройки игры'''

            menuSelectNotExists = 'Данной функции не существует'

            gameSettingsTitle = '''\nНастройки игры
    0) Нажмите клавишу Z, чтобы вернуться назад
    1) Нажмите клавишу L, чтобы поменять язык игры'''


            break


        else:
            print(dataIncorrectEng)

def gameLoop():
    while True:
        print(menuScreen)
        userSelect = input('> ')

        if userSelect in menuSelect:
            if userSelect == menuSelect[0] or userSelect == menuSelect[1] or userSelect == menuSelect[2]:
                print('Start Game')

            elif userSelect == menuSelect[3] or userSelect == menuSelect[4] or userSelect == menuSelect[5]:
                sys.exit()

            elif userSelect == menuSelect[6] or userSelect == menuSelect[7] or userSelect == menuSelect[8]:

                while True:
                    print(gameSettingsTitle)
                    userSelect = input('> ')

                    if userSelect == menuSelectSetting[0] or userSelect ==  menuSelectSetting[1] or userSelect == menuSelectSetting[2]:
                        break

                    elif userSelect == menuSelectSetting[3] or userSelect ==  menuSelectSetting[4] or userSelect == menuSelectSetting[5]:
                        languageSelection()


        elif userSelect in menuSelectForEditor:
            if userSelect == menuSelectForEditor[0]:
                adminAuth()

        else:
            print(menuSelectNotExists)
            continue


def update():
    pass


def render():
    languageSelection()
    gameLoop()


# def gameWin():
#     attempts += 1

#     print('\nТы справился, тебе добовляется 1 попытка, у тебя:', attempts)

#     return attempts


# def gameLose():
#     attempts -= 1
#     print('\nОтвет не верный, минуc 1 попытка, у тебя осталось:', attempts)

#     if attempts <= 0:
#         print('\nТы проиграл. :(')
#         # выход или предложение поиграть с точки сохранения
#         sys.exit()

#     return attempts


# def gameLevel_1():
#     print('\nЗадача 1')
#     print(
#     8631 = 3
#     3625 = 1
#     9612 = 2
#     7831 = x)

#     while True:
#         x = input('\nВведите значение x (int)\n> ')

#         if x == '2':
#             gameWin()
#             global listLevel
#             listLevel.append(1)
#             break

#         # подсчет сколько попыток понадобилось для прохождения
#         # выводить значение в главном меню -> пройденые уровни

#         else:
#             gameLose()


if __name__ == "__main__":
    render()
